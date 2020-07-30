from django.contrib import admin

# Register your models here.


# Importar modelos
from core.models import (Shelter)
from core.models import (Visit)
from core.models import (Specie)
from core.models import (Rol)
from core.models import (Person)
from core.models import (Tour)
from core.models import (Single)
from core.models import (Single_Tour)
from core.models import (Employee)


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