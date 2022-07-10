from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    # path("common/", include("apps.common.urls")),
    path("users/", include("apps.users.urls")),
    path("", include("apps.nomenclature.urls")),
    path("", include("apps.promotions.urls")),
    path("", include("apps.orders.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

