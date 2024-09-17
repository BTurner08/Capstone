from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address_street = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_number = models.CharField(max_length=200, blank=True, null=True)
    address_state = models.CharField(max_length=200)
    address_zipcode = models.CharField(max_length=12)
    
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username