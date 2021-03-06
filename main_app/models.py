from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COLORS = (
    ('Pink', 'Pink'),
    ('Red', 'Red'),
    ('Orange', 'Orange'),
    ('Beige', 'Beige'),
    ('Yellow', 'Yellow'),
    ('Green', 'Green'),
    ('Light Blue', 'Light Blue'),
    ('Dark Blue', 'Dark Blue'),
    ('Purple', 'Purple'),
    ('Brown', 'Brown'),
    ('Grey', 'Grey')
    )

TYPE = (
    ('T-Shirt', 'T-Shirt'),
    ('Sweater', 'Sweater'),
    ('Sweatshirt', 'Sweatshirt'),
    ('Jacket', 'Jacket'),
    ('Jeans', 'Jeans'),
    ('Leggings', 'Leggings'), 
    ('Shorts', 'Shorts'),
    ('Dress Pants', 'Dress Pants'),
    ('Dress', 'Dress'),
    ('Skirt', 'Skirt'),
    ('Blouse', 'Blouse'),
    ('Parka', 'Parka'),
    ('Coat', 'Coat'),
    ('Tank Top', 'Tank Top'),
    )

SEASON = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Fall', 'Fall'),
    ('Winter', 'Winter'),
    )

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE, default=TYPE[0][0])
    color = models.CharField(max_length=10, choices=COLORS, default=COLORS[0][0])
    season = models.CharField(max_length=10, choices=SEASON, default=SEASON[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for clothing_id: {self.clothing_id} @{self.url}"