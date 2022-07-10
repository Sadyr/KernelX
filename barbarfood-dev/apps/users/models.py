import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _  # noqa
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager
from config.settings import Languages
from apps.common.models import TimestampModel
from .utils import calculate_age
from ..orders.models import Cart


class User(PermissionsMixin, AbstractBaseUser):
    class Meta:
        verbose_name = _("Учетная запись")
        verbose_name_plural = _("Учетная запись")

    mobile_phone = PhoneNumberField(_("Моб. телефон"), unique=True, null=True)
    username = models.CharField("Username", max_length=100, unique=True, null=False)
    name = models.CharField(_("Имя"), max_length=256, null=True)
    email = models.EmailField(null=True)
    birth_date = models.DateField(_("Дата рождения"), blank=True, null=True)
    tdid = models.CharField(_("Юзер иденфикатор"), max_length=250, null=True)
    language = models.CharField(_("Язык"), max_length=20, choices=Languages.choices, default=settings.DEFAULT_LANGUAGE)
    is_active = models.BooleanField(_("Активный"), default=True)
    is_staff = models.BooleanField(_("Сотрудник"), default=False)
    secret_key = models.UUIDField(_("Секретный ключ"), default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(_("Создан"), default=timezone.now)
    updated_at = models.DateTimeField(_("Обновлен"), auto_now=True)

    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    @property
    def age(self):
        return calculate_age(self.birth_date)


class Address(models.Model):

    district = models.CharField(_("Район"), max_length=255, null=True, blank=True)
    street = models.CharField(_("Улица"), max_length=255, null=True, blank=True)
    building = models.CharField(_("Дом / здание"), max_length=100, blank=True)
    is_private_home = models.BooleanField(_('Частный дом'), default=False)
    entrance = models.CharField(_("Подъезд"), max_length=100, null=True, blank=True)
    floor = models.CharField(_("Этаж"), max_length=100, null=True, blank=True)
    flat = models.CharField(_("Квартира"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class UserSession(models.Model):
    uuid = models.UUIDField("Идентификатор", default=uuid.uuid4, unique=True, editable=False)
    session_id = models.TextField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=False, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=False)