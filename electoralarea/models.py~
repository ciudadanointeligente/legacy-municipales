from django.db import models

# Create your models here.
class ElectionZone(models.Model):
	name = models.CharField(max_length = 200)
	class Meta:
		abstract = True
		ordering = ['name']
	

class Circunscripcion(ElectionZone):
	# name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class District(ElectionZone):
	circunscripcion = models.ForeignKey('Circunscripcion')
	# name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Comuna(ElectionZone):
	region = models.ForeignKey('Region')
	district = models.ForeignKey('District')
	# name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Region(ElectionZone):
	# name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name
	
