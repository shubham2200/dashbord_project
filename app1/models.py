from os import name
from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=200 , null= True)
    phone = models.CharField(max_length=200 , null= True)
    email = models.CharField(max_length=200 , null= True)
    date_created = models.DateTimeField(auto_now_add=True , null= True)

    def __str__(self):
        return self.name


class products(models.Model):
    CATEGORY =(
        ('Indoor' , 'Indoor'),
        ('out Door' , 'out door'),
    )
    name = models.CharField(max_length=200 , null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200 , null=True , choices=CATEGORY)
    description = models.CharField(max_length=200 , null=True)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    def __str__(self):
        return self.name


class tag(models.Model):
    name = models.CharField(max_length=200 , null= True)
  
    def __str__(self):
        return self.name





class order(models.Model):
    STATUS = (
        ('pending' , 'pending'),
        ('out of delivery',' out of delivery'),
        ('delivered','delivered'),
    )
    costomer = models.ForeignKey(customer ,null=True , on_delete=SET_NULL)
    product = models.ForeignKey(products , null=True , on_delete=SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    status = models.CharField(max_length=200 , null=True , choices=STATUS)
    tags = models.ManyToManyField(tag)

