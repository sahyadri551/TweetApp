from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/",blank=True,null=True)
    bio = models.TextField(blank=True)
    dob = models.DateField(blank=True,null=True)
    nationality = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=250,blank=True)
    mobile = models.CharField(max_length=14,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)
    profession = models.CharField(max_length=50,blank=True)

    class Meta:
        ordering = ['-created_at','-modified_at']
    

    def __str__(self):
        return self.user.username
    

