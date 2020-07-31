"""
Enpoints de la API
"""
# Django imports
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

# Rest_framework imports
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


# Local imports
# Modelos
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

# Serializadores
from core.serializers import (Shelter_Serializer,
                              Visit_Serializer,
                              Specie_Serializer,
                              Rol_Serializer,
                              Person_Serializer,
                              Tour_Serializer,
                              Single_Serializer,
                              Single_Tour_Serializer,
                              Employee_Serializer)



# Other imports
# ...
class Shelter_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Shelter
    """
    queryset = Shelter.objects.all()
    serializer_class = Shelter_Serializer


class Visit_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Visit
    """
    queryset = Visit.objects.all()
    serializer_class = Visit_Serializer


class Specie_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Specie
    """
    queryset = Specie.objects.all()
    serializer_class = Specie_Serializer


class Rol_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Rol
    """
    queryset = Rol.objects.all()
    serializer_class = Rol_Serializer


class Person_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Person
    """
    queryset = Person.objects.all()
    serializer_class = Person_Serializer


class Tour_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Tour
    """
    queryset = Tour.objects.all()
    serializer_class = Tour_Serializer


class Single_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Single
    """
    queryset = Single.objects.all()
    serializer_class = Single_Serializer


class Single_Tour_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Single_Tour
    """
    queryset = Single_Tour.objects.all()
    serializer_class = Single_Tour_Serializer


class Employee_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Employee
    """
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
