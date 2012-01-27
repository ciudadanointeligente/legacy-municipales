# coding= utf-8
from django.core.management.base import BaseCommand, CommandError
import csv


class CsvReader(object):
    def detectRegion(self, line):
        from electoralarea.models import Region
        region, created = Region.objects.get_or_create(name = line[0])
        return region

    
    def detectCircunscripcion(self, line):
        from electoralarea.models import Circunscripcion
        circunscripcion, created = Circunscripcion.objects.get_or_create(name = line[1])
        return circunscripcion


    def detectDistrict(self, line):
        from electoralarea.models import District
        circunscripcion = self.detectCircunscripcion(line)
        district, created = District.objects.get_or_create(name = line[2], circunscripcion= circunscripcion)
        return district
    

    def detectComuna(self, line):
        from electoralarea.models import Comuna
        region = self.detectRegion(line)
        district = self.detectDistrict(line)
        comuna = Comuna.objects.create(name = line[3], region = region, district = district)
        return comuna


class DivisionElectoralImporter(BaseCommand):
    def handle(self, *args):
        reader = csv.reader(open(args[0], 'rb'), delimiter=',')
        csvReader = CsvReader()
        for line in reader:
            comuna = csvReader.detectComuna(line)
