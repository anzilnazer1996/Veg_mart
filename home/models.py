from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vegetables(models.Model):
    item=models.CharField(max_length=50,unique=True)
    price=models.FloatField()
    status=models.CharField(max_length=12)
    veg_images=models.ImageField(upload_to='veg_images')
    def __str__(self):
        return self.item
class Userinfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')
    def __str__(self):
        return self.user.username       