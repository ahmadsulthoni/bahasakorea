from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,PermissionsMixin

from .manager import UserManager

class Users(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    #setting field

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    #user manager
    objects = UserManager()

    class Meta:
        abstract = False

