from django.db import models
from electoralarea.models import Comuna

class Dimension(models.Model):
    name = models.CharField(max_length=255)


class SubDimension(models.Model):
    name = models.CharField(max_length=255)
    dimension = models.ForeignKey(Dimension)


class Variable(models.Model):
    name = models.CharField(max_length=255)
    subdimension = models.ForeignKey(SubDimension)


class Description(models.Model):
    description = models.CharField(max_length=255)
    variable = models.ForeignKey(Variable)


class LecturaResultadoText(models.Model):
    comuna = models.ForeignKey(Comuna)
    description = models.ForeignKey(Description)
    value = models.TextField()