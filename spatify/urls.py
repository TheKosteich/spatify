from django.conf.urls import handler404, handler500  # noqa
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from spatify import settings

handler404 = 'spatify.views.page_not_found'  # noqa
handler500 = 'spatify.views.server_error'  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Django urls setting for development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
