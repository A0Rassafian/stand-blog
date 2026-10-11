from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Profile (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    father_name = models.CharField(max_length =25 )
    melicode = models.CharField(max_length =10)
    image = models.ImageField(upload_to='images/profiles' , null=True,blank=True)
    def __str__(self):
        return self.user.username