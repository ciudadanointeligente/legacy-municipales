# -*- coding: utf-8 -*-
from django.test import TestCase
from areas_municipales.models import Dimension, SubDimension, Variable, Description, LecturaResultadoText
from electoralarea.models import Comuna, Region, District, Circunscripcion

class DimensionTest(TestCase):
    def test_dimension_creation(self):
        dimension = Dimension(name=u"caracterización")

        self.assertTrue(isinstance(dimension,Dimension))
        self.assertEqual(dimension.name,u'caracterización')


class SubDimensionTest(TestCase):
    def test_subdimension_create(self):
        dimension = Dimension(name=u'caracterización')
        subdimension = SubDimension(name=u'Administración municipal',dimension=dimension)

        self.assertTrue(isinstance(subdimension,SubDimension))
        self.assertEqual(subdimension.name,u'Administración municipal')
        self.assertEqual(subdimension.dimension,dimension)


class VariableTest(TestCase):
    def test_variable_create(self):
        dimension = Dimension(name=u'caracterización')
        subdimension = SubDimension(name=u'Administración municipal',dimension=dimension)
        variable = Variable(name=u"identificación del alcalde", subdimension = subdimension)

        self.assertTrue(isinstance(variable, Variable))
        self.assertEqual(variable.name,u"identificación del alcalde")
        self.assertEqual(variable.subdimension, subdimension)

class DescriptionTest(TestCase):
    def test_create_a_description(self):
        dimension = Dimension(name=u'caracterización')
        subdimension = SubDimension(name=u'Administración municipal',dimension=dimension)
        variable = Variable(name=u"identificación del alcalde", subdimension = subdimension)


        description = Description(description=u"Nombre Alcalde",variable=variable)

        self.assertTrue(isinstance(description,Description))
        self.assertEqual(description.description,u"Nombre Alcalde")
        self.assertEqual(description.variable, variable)


class TextValueTest(TestCase):
    def setUp(self):
        circunscripcion, created = Circunscripcion.objects.get_or_create(name='circunscripcion 1')
        district, created = District.objects.get_or_create(name='district 1', circunscripcion = circunscripcion)
        region, created = Region.objects.get_or_create(name='region 1')
        self.comuna, created = Comuna.objects.get_or_create(name='comuna 1', region = region, district = district)

        dimension = Dimension(name=u'caracterización')
        subdimension = SubDimension(name=u'Administración municipal',dimension=dimension)
        variable = Variable(name=u"identificación del alcalde", subdimension = subdimension)


        self.description = Description(description=u"Nombre Alcalde",variable=variable)



    def test_create_a_value_relating_it_to_a_comuna(self):
        lectura_resultado = LecturaResultadoText(comuna=self.comuna,description = self.description, value=u"alcalde bacán")



        self.assertTrue(isinstance(lectura_resultado, LecturaResultadoText))
        self.assertEqual(lectura_resultado.comuna, self.comuna)
        self.assertEqual(lectura_resultado.description, self.description)
        self.assertEqual(lectura_resultado.value,u"alcalde bacán")









