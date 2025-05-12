from django.db import models

# Create your models here.

# Base class for created/updated timestamps
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name

class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"

