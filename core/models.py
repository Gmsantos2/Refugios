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

    salary = models.DecimalField()
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
    





