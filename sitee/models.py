from django.db import models

# Create your models here.
from django.utils.text import slugify

from sitee import price_choices, color_choices


class Category(models.Model):
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    icon = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Product(models.Model):
    name = models.CharField(max_length=512)
    price = models.IntegerField()
    price_type = models.CharField(max_length=5, choices=price_choices())
    color = models.CharField(max_length=50, choices=color_choices())
    size = models.JSONField(default={'len': 0, 'height': 0, 'width': 0})
    short_description = models.TextField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.product.name









