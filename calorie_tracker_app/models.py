from django.db import models

# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calorie_count = models.IntegerField()

    def __str__(self):
        return self.name
