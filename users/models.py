from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, is_admin=False, is_staff=False, is_active=True,**extra_fields):
        if not phone_number:
            raise ValueError("User must have an phone number")
    

        user = self.model(
            phone_number=phone_number
        )
     
        user.name = name
        # user.set_password(password)  # change password to hash
        user.set_password('')
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, phone_number, password, name,**extra_fields):
        if not phone_number:
            raise ValueError("User must have an phone number")
    

        user = self.model(
            phone_number=phone_number
        )
     
        user.name = name
        # user.set_password(password)  # change password to hash
  
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):

    username=None
    phone_number=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=32)
    profile_picture=models.URLField(max_length=1000)

    USERNAME_FIELD = "phone_number"   # e.g: "username", "email"
    REQUIRED_FIELDS = ['name',]

    objects=UserManager()


    def __str__(self):
      return self.name


