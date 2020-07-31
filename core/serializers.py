"""
Los serializadores permiten parsear la información en ambos sentidos, la que
se recibe en los request y la que se envía. Esto nos será util cuando queramos
enviar infromacion en formato json
"""

# Django imports
# ..

# Rest_framework imports
from rest_framework import serializers


# Local imports
from core.models import (Shelter,
                        Visit,
                        Specie,
                        Rol,
                        Person,
                        Tour,
                        Single,
                        Single_Tour,
                        Employee)

# Other imports
# ...


class Shelter_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Shelter
    """
    class Meta:
        model = Shelter
        fields = "__all__"


class Visit_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Visit
    """
    class Meta:
        model = Visit
        fields = "__all__"


class Specie_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Specie
    """
    class Meta:
        model = Specie
        fields = "__all__"



class Rol_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Rol
    """
    class Meta:
        model = Rol
        fields = "__all__"

    
class Person_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Person
    """
    class Meta:
        model = Person
        fields = "__all__"


class Tour_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Tour
    """
    class Meta:
        model = Tour
        fields = "__all__"


class Single_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Single
    """
    class Meta:
        model = Single
        fields = "__all__"


class Single_Tour_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Single_Tour
    """
    class Meta:
        model = Single_Tour
        fields = "__all__"


class Employee_Serializer(serializers.ModelSerializer):
    """
    Serializador del modelo Employee
    """
    class Meta:
        model = Employee
        fields = "__all__"
