import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "CRUD_project.settings")

import django
django.setup()

from CRUD_app.models import Student
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fSno = randint(11,50)
        fSname = faker.name()
        fSclass = randint(1,12)
        fSaddress = faker.city()
        record = Student.objects.get_or_create(Sno = fSno, Sname = fSname, Sclass = fSclass, Saddress = fSaddress)

generate(30)