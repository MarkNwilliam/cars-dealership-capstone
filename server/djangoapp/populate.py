import os
import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()

from djangoapp.models import CarMake, CarModel


car_make_data = [
    {
        "name": "Toyota",
        "description": "Japanese multinational automotive manufacturer."
    },
    {
        "name": "Honda",
        "description": "Japanese public multinational conglomerate manufacturer."
    },
    {
        "name": "Ford",
        "description": "American multinational automaker."
    },
    {
        "name": "BMW",
        "description": "German multinational luxury vehicle manufacturer."
    },
    {
        "name": "Mercedes-Benz",
        "description": "German luxury and commercial vehicle automotive brand."
    },
    {
        "name": "Audi",
        "description": "German automotive manufacturer of luxury vehicles."
    },
    {
        "name": "Chevrolet",
        "description": "American automobile division of General Motors."
    },
]

car_model_data = [
    ("Toyota", "Camry", "SEDAN", 2022, 1),
    ("Toyota", "Corolla", "SEDAN", 2021, 1),
    ("Toyota", "RAV4", "SUV", 2023, 2),
    ("Honda", "Civic", "SEDAN", 2022, 3),
    ("Honda", "Accord", "SEDAN", 2021, 4),
    ("Honda", "CR-V", "SUV", 2023, 2),
    ("Ford", "Mustang", "COUPE", 2022, 5),
    ("Ford", "F-150", "PICKUP", 2023, 6),
    ("Ford", "Explorer", "SUV", 2021, 4),
    ("BMW", "3 Series", "SEDAN", 2022, 7),
    ("BMW", "X5", "SUV", 2023, 2),
    ("BMW", "M4", "COUPE", 2021, 8),
    ("Mercedes-Benz", "C-Class", "SEDAN", 2022, 9),
    ("Mercedes-Benz", "E-Class", "SEDAN", 2021, 10),
    ("Mercedes-Benz", "GLE", "SUV", 2023, 2),
    ("Audi", "A4", "SEDAN", 2022, 11),
    ("Audi", "Q5", "SUV", 2021, 12),
    ("Audi", "RS5", "COUPE", 2023, 2),
    ("Chevrolet", "Malibu", "SEDAN", 2022, 13),
    ("Chevrolet", "Equinox", "SUV", 2021, 4),
    ("Chevrolet", "Camaro", "COUPE", 2023, 14),
]


@transaction.atomic
def initiate():
    print("Clearing existing data...")
    CarModel.objects.all().delete()
    CarMake.objects.all().delete()

    print("Populating car makes and models...")
    for make in car_make_data:
        CarMake.objects.create(**make)

    for make_name, name, type, year, dealer_id in car_model_data:
        car_make = CarMake.objects.get(name=make_name)
        CarModel.objects.create(
            car_make=car_make,
            name=name,
            type=type,
            year=year,
            dealer_id=dealer_id
        )

    print("Populate complete:",
          CarMake.objects.count(), "makes,",
          CarModel.objects.count(), "models")
