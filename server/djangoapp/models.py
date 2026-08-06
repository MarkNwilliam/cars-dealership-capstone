from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "Name: " + self.name + "," + \
            " Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('MINIVAN', 'Minivan'),
        ('PICKUP', 'Pickup'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('SPORTS', 'Sports'),
        ('LUXURY', 'Luxury'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    dealer_id = models.IntegerField(default=0)

    def __str__(self):
        return "Name: " + self.name + "," + \
            " Make: " + self.car_make.name + "," + \
            " Type: " + self.type + "," + \
            " Year: " + str(self.year)
