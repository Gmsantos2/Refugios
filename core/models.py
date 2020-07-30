from django.db import models

# Create your models here.

class Shelter(models.Model):

    meters = models.IntegerField()
    city = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Visit(models.Model):

    pass


class Specie(models.Model):

    pass


class Rol(models.Model):

    pass


class Person(models.Model):

    pass


class Tour(models.Model):

    pass


class Single(models.Model):

    pass


class Single_Tour(models.Model):

    pass  


class Employee(models.Model):

    pass
    