"""
Se registran las rutas de la aplicacion. En este caso usamos el módulo 'router'
de la libreria djangorestframework para que genere las url correspondientes 
para cada modelo automaticamente
"""

# Django
from django.conf import settings
from django.urls import path, include

# Rest framewkor imports
# ...

# Local project imports
from core.router import router
from core import views


# Other impoprts
# ...


urlpatterns = [

    # Rutas correspondientes a todos los modelos en general
    path('', include(router.urls)),


]