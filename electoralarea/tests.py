# coding= utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from electoralarea.models import Circunscripcion
from electoralarea.models import District
from electoralarea.models import Comuna
from electoralarea.models import Region
from electoralarea.management.commands.division_electoral_importer import *

class CircuscripcionTest(TestCase):
	def test_create_circunscripcion(self):
		#create circunscripcion from scratch
		circunscripcion, created = Circunscripcion.objects.get_or_create(name='circunscripcion 1')
		self.assertTrue(created)
		self.assertTrue(circunscripcion.name=='circunscripcion 1')
	
class DistrictTest(TestCase):
	def test_create_district(self):
		circunscripcion, created = Circunscripcion.objects.get_or_create(name='circunscripcion 1')
		district, created = District.objects.get_or_create(name='district 1', circunscripcion = circunscripcion)
		self.assertTrue(created)
		self.assertTrue(district.name=='district 1')
		self.assertTrue(circunscripcion.name=='circunscripcion 1')

class RegionTest(TestCase):
	def test_create_region(self):
		#create region from scratch
		region, created = Region.objects.get_or_create(name='region 1')
		self. assertTrue(created)
		self.assertTrue(region.name=='region 1')
		
class ComunaTest(TestCase):
	def test_create_comuna(self):
		#create comuna from scratch
		circunscripcion, created = Circunscripcion.objects.get_or_create(name='circunscripcion 1')
		district, created = District.objects.get_or_create(name='district 1', circunscripcion = circunscripcion)
		region, created = Region.objects.get_or_create(name='region 1')
		comuna, created = Comuna.objects.get_or_create(name='comuna 1', region = region, district = district)
		self.assertTrue(created)
		self.assertTrue(comuna.name=='comuna 1')
		self.assertTrue(comuna.region.name == 'region 1')
		self.assertTrue(comuna.district.name == 'district 1')
		self.assertTrue(comuna.district.circunscripcion.name == 'circunscripcion 1')


class CsvReaderTestOneLine(TestCase):
        def setUp(self):
                self.csvreader = CsvReader()
                self.line = [u'XV Región de Arica y Parinacota', u'I - Tarapacá', u'Distrito Número 1', u'Arica']

        def test_detect_region_out_of_a_line(self):
                region = self.csvreader.detectRegion(self.line)
                self.assertEqual(Region.objects.count(),1)
                self.assertEqual(region.name,u'XV Región de Arica y Parinacota')
        
        def test_detect_cisctunscripcion_out_of_a_line(self):
                circunscripcion = self.csvreader.detectCircunscripcion(self.line)
                self.assertEqual(Circunscripcion.objects.count(),1)
                self.assertEqual(circunscripcion.name, u'I - Tarapacá')

        def test_detect_district_out_of_a_line(self):
                district = self.csvreader.detectDistrict(self.line)
                self.assertEqual(District.objects.count(),1)
                self.assertEqual(district.name, u'Distrito Número 1')
                self.assertEqual(district.circunscripcion.name, u'I - Tarapacá')
       
        def test_detect_comuna_out_of_a_line(self):
                comuna = self.csvreader.detectComuna(self.line)
                self.assertEqual(Comuna.objects.count(),1)
                self.assertEqual(comuna.name, u'Arica')
                self.assertEqual(comuna.district.name, u'Distrito Número 1')
                self.assertEqual(comuna.region.name, u'XV Región de Arica y Parinacota')

class CsvReaderTwoLines(TestCase):
       def setUp(self):
               self.csvreader = CsvReader()
               line = [u'XV Región de Arica y Parinacota', u'I - Tarapacá', u'Distrito Número 1', u'Arica']
               comuna = self.csvreader.detectComuna(line)
               self.camarones = [u'XV Región de Arica y Parinacota', u'I - Tarapacá', u'Distrito Número 1', u'Camarones']

       def test_create_a_new_comuna_but_no_new_circunscripcion_district_nor_region(self):
               camarones = self.csvreader.detectComuna(self.camarones)
               self.assertEqual(Comuna.objects.count(),2) #there are 2 comunas now Arica and Camarones
               self.assertEqual(Region.objects.count(),1)
               self.assertEqual(Circunscripcion.objects.count(),1)
               self.assertEqual(District.objects.count(),1)
               self.assertEqual(camarones.name, u'Camarones')


class CommandTest(TestCase):
    def setUp(self):
        pass

    def test_read_csv_and_create_data(self):
        args = ('electoralarea/data/division_electoral.csv',)
        command = Command()
        command.handle(*args)
        self.assertTrue(Comuna.objects.count() > 0)
        self.assertTrue(Circunscripcion.objects.count() > 0)
        self.assertTrue(District.objects.count() > 0)
        self.assertTrue(Region.objects.count() > 0)

