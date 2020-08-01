"""
Aqui se registran los modelos para que puedan ser tratados en el dashboard de administracion
de django
"""
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
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


# Registrar los modelos con la plantilla de django-import-export
# Esta plantilla permite descargar la información en los siguientes formatos
# - csv
# - xls
# - xlsx
# - tsv
# - ods
# - json
# - yaml
# - html
@admin.register(Shelter)
class ShelterAdmin(ImportExportModelAdmin):
    pass

@admin.register(Visit)
class VisitAdmin(ImportExportModelAdmin):
    pass

@admin.register(Specie)
class SpecieAdmin(ImportExportModelAdmin):
    pass

@admin.register(Rol)
class RolAdmin(ImportExportModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Tour)
class TourAdmin(ImportExportModelAdmin):
    pass

@admin.register(Single)
class SingleAdmin(ImportExportModelAdmin):
    pass

@admin.register(Single_Tour)
class Single_TourAdmin(ImportExportModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass
