from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
