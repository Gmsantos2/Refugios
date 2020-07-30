from django.db import models

# Create your models here.

class Shelter(models.Model):

    meters = models.IntegerField()
    city = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Visit(models.Model):
    shelter = models.IntegerField()
    date = models.DateTimeField()

class Specie(models.Model):
    type_specie = models.CharField(max_length=255)
    habitat = models.CharField(max_length=255)
    endangered = models.BooleanField()


class Rol(models.Model):
    description = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    age = models.IntegerField()


class Tour(models.Model):

    pass


class Single(models.Model):

    pass


class Single_Tour(models.Model):

    pass  


class Employee(models.Model):

    pass
    