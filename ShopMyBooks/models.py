from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='shop/pics')
    rating = models.FloatField(default="")
    price = models.FloatField()

    #it will show the product with product name in admin page
    def __str__(self):
        return self.product_name