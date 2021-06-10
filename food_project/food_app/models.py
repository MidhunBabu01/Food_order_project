from django.db import models

# Create your models here.


class FoodDetails(models.Model):

    def __str__(self):
        return self.food_name

    food_choices = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
    )
    category = models.CharField(max_length=50,choices=food_choices, default="1")
    food_name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="pictures")
    old_price = models.IntegerField()   
    new_price = models.IntegerField()   
    desc = models.TextField()
    big_desc = models.TextField() 


