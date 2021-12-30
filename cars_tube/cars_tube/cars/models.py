from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    mileage = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )

    FUEL_CHOICE_DIESEL = 'diesel'
    FUEL_CHOICE_PETROL = 'petrol'
    FUEL_CHOICE_HYBRID = 'hybrid'
    FUEL_CHOICE_GAS = 'gas'

    fuel = models.CharField(choices=(
        (FUEL_CHOICE_DIESEL, 'Diesel'),
        (FUEL_CHOICE_PETROL, 'Petrol'),
        (FUEL_CHOICE_HYBRID, 'Hybrid'),
        (FUEL_CHOICE_GAS, 'Gas')
    ),
    max_length=10
    )