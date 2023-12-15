from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
from django.db import models


# Create your models here.
class Seller(models.Model):
    seller = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=200)
    parents = models.ForeignKey("self", on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    price = models.IntegerField()


class Order(models.Model):
    code = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cast = models.IntegerField()


class OrderItem(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
