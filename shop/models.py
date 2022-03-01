from django.db import models

# Create your models here.


class Products(models.Model):

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    catagory = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title