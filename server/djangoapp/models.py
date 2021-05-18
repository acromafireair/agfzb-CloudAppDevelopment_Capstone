from django.db import models
from django.utils.timezone import now


# Create your models here.

# Car Make, the __str__ method just returns the name of the car make
class CarMake(models.Model):
    name=models.CharField(primary_key=True,max_length=25)
    description=models.CharField(max_length=150)
    def __str__(self):
        return name


# Car Model, the __str__ method returns the car's year, make, and model
class CarModel(models.Model):
    CAR_TYPES=[
        ("SUV", "SUV"),
        ("Truck", "Truck"),
        ("Sedan", "Sedan"),
        ("Van", "Van"),
        ("Coupe", "Coupe"),
        ("Wagon", "Wagon"),
        ("Convertible", "Convertible"),
        ("Sports Car", "Sports Car"),
        ("Diesel", "Diesel"),
        ("Crossover", "Crossover"),
        ("Luxury Car", "Luxury Car"),
        ("Hybrid/Electric", "Hybrid/Electric")
    ]
    make=models.ManyToManyField(CarMake)
    name=models.CharField(max_length=50)
    dealer_id=models.IntegerField()
    car_type=models.CharField(max_length=20,choices=CAR_TYPES)
    car_year=models.IntegerField()
    def __str__(self):
        return year + " " + make + " " + name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
