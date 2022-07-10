from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from apps.pipeline.models import ServiceHistory


class HiddenAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}  # Hide model in admin list


class ChangeOnlyMixin:
    def has_add_permission(self, request, obj=None):
        return False


class ReadOnlyMixin(ChangeOnlyMixin):
    def has_change_permission(self, request, obj=None):
        return False


class ReadChangeOnlyMixin():
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class ReadChangeOnlyTabularInline(ReadChangeOnlyMixin, admin.TabularInline):
    ...


class ReadChangeOnlyStackedInline(ReadChangeOnlyTabularInline, admin.StackedInline):
    ...


class HistoryInline(ReadOnlyMixin, GenericTabularInline):
    model = ServiceHistory
    fields = ["service", "service_pretty", "runtime", "created_at", "show"]
    readonly_fields = ["show", "created_at"]
    classes = ("collapse",)

    def show(self, obj):
        url = reverse("admin:pipeline_servicehistory_change", args=(obj.pk,))  # noqa
        return mark_safe(f"<a href='{url}'>Посмотреть</a>")

    show.short_description = _("Лог сервиса")