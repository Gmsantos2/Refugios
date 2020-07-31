# Django importaciones
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

# Rest_framework importaciones
# ...


urlpatterns = [
    path('admin/', admin.site.urls),                                        # Url del administrador
    path('api/', include('core.urls')),                                # Inlcuimos las urls de la app core
]
