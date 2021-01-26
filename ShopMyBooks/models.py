from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to='pics')
    rating = models.IntegerField()
    price = models.FloatField()