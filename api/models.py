from django.db import models

# Create your models here.

class Coffee(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(decimal_places=2,max_digits=5)
    description=models.CharField(max_length=512)
    imageUrl=models.URLField(default="")


    def __str__(self) -> str:
        return self.name

class CoffeeCategory(models.Model):
    name=models.CharField(max_length=24)
    coffees=models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.name


