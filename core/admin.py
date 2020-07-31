from django.contrib import admin

# Register your models here.


# Importar modelos
from core.models import (Shelter,
                        Visit,
                        Specie,
                        Rol,
                        Person,
                        Tour,
                        Single,
                        Single_Tour,
                        Employee)


# Registrar los modelos
admin.site.register(Shelter)
admin.site.register(Visit)
admin.site.register(Specie)
admin.site.register(Rol)
admin.site.register(Person)
admin.site.register(Tour)
admin.site.register(Single)
admin.site.register(Single_Tour)
admin.site.register(Employee)