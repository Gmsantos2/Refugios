"""
El modulo 'routers' nos ayuda creando las rutas
comunes para todos los modelos, incluyendo los métodos http:
GET, UPDATE, POST, DELETE
"""
# Django imports

# Rest_framework imports
from rest_framework import routers

# Local imports
from core.views import (Shelter_Viewset,
                         Visit_Viewset,
                         Specie_Viewset,
                         Rol_Viewset,
                         Person_Viewset,
                         Tour_Viewset,
                         Single_Viewset,
                         Single_Tour_Viewset,
                         Employee_Viewset)


# Other imports
# ...


router = routers.DefaultRouter()

router.register('shelter', Shelter_Viewset)
router.register('visit', Visit_Viewset)
router.register('specie', Specie_Viewset)
router.register('rol', Rol_Viewset)
router.register('person', Person_Viewset)
router.register('tour', Tour_Viewset)
router.register('single', Single_Viewset)
router.register('single_tour', Single_Tour_Viewset)
router.register('employee', Employee_Viewset)


