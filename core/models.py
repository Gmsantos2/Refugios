"""
Modelos que representan la tabal en la base de datos
"""
from django.db import models

# Create your models here.

class Shelter(models.Model):
    """
    """

    meters = models.IntegerField()
    city = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Visit(models.Model):
    """
    """

    shelter = models.IntegerField()
    date = models.DateTimeField()

class Specie(models.Model):
    """
    """

    type_specie = models.CharField(max_length=255)
    habitat = models.CharField(max_length=255)
    endangered = models.BooleanField()


class Rol(models.Model):
    """
    """

    description = models.CharField(max_length=255)


class Person(models.Model):
    """
    """

    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    age = models.IntegerField()


class Tour(models.Model):
    """
    """

    estimated_time = models.IntegerField()
    max_visitors = models.IntegerField()


class Single(models.Model):
    """
    """

    nickname = models.CharField(max_length=255)
    age = models.IntegerField()
    origin = models.CharField(max_length=255)
    born_date = models.DateField()
    born_place = models.CharField(max_length=255)

    specie = models.ForeignKey(to=Specie,
        blank=False,
        null=False,
        on_delete=models.PROTECT)

    shelter = models.ForeignKey(to=Shelter,
        blank=False,
        null=False,
        on_delete=models.PROTECT)


class Single_Tour(models.Model):
    """
    """

    single = models.ForeignKey(to=Single,
        blank=False,
        null=False,
        on_delete=models.PROTECT)

    tour = models.ForeignKey(to=Tour,
        blank=False,
        null=False,
        on_delete=models.PROTECT)

 


class Employee(models.Model):
    """
    """

    salary = models.DecimalField(max_digits=10, decimal_places=2)
    time_enter = models.CharField(max_length=100,
                                   blank=True,
                                   null=True)
    time_exit = models.CharField(max_length=100,
                                    blank=True,
                                   null=True)

    person = models.ForeignKey(to=Person,
        blank=False,
        null=False,
        on_delete=models.PROTECT)

    rol = models.ForeignKey(to=Rol,
        blank=False,
        null=False,
        on_delete=models.PROTECT)

    shelter = models.ForeignKey(to=Shelter,
        blank=False,
        null=False,
        on_delete=models.PROTECT)
    





