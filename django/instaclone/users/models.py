from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone_number = models.CharField(max_length=10, unique=True)
    is_Active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    DEFAULT_PROFILE_PIC_URL = "https://placeholdersite.com/placeholder.png"
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    bio = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
