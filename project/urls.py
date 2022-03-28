from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include
from django.conf import settings
from . import settings

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', include('pages.urls')),
    path('product/', include('product.urls')),
    path('', include('account.urls')),
    path('reserve/', include('reserve.urls')),
    path('admin/', include('adminportal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
