from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from api.manager import UserManager
# Create your models here.
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations: True
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")

        email=self.normalize_email(email)
        user=self.model(email=email ,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user must have is_staff True")
        return self.create_user(email,password,**extra_fields)
        


class user(AbstractUser):
    username=None
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=14)
    is_verified=models.BooleanField(default=False)
    email= models.EmailField(unique=True)
    company_or_indvidual=models.CharField(max_length=21)
    #is_indvidual=models.BooleanField(default=False)
    #is_company=models.BooleanField(blank=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    #password=models.CharField(max_length=50)
    standard_or_custom=models.CharField(max_length=21,null=True,blank=True)
    # is_standard=models.BooleanField(default=True)
    # is_custom=models.BooleanField(default=False)
    forget_password=models.CharField(max_length=50,null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)

    objects=UserManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    #REQUIRED_FIELDS=["username"]