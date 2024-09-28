from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

class Category(models.Model):
    Name= models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateField(auto_created=True)
    # Note: images need pillow to be installed (python3 -m pip install pillow)
    image = models.ImageField(upload_to="images/posts/", null=True, blank = True)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    

class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name
    