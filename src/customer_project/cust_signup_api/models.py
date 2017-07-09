from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class CustomersManager(BaseUserManager):
    """Helps Django work with our custom customer model."""

    def create_user(self, email, first_name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        cust = self.model(email=email, first_name=first_name)

        cust.set_password(password)
        cust.save(using=self._db)

        return cust

    def create_superuser(self, email, first_name, password):
        """"Creates and saves a new superuser with given details."""

        cust = self.create_user(email, name, password)

        cust.is_superuser = True
        cust.is_staff = True

        cust.save(using=self._db)

        return cust

class Customers(AbstractBaseUser,PermissionsMixin):
    """Represents customer table which has information for signup"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        """"Used to get a users full name."""

        return self.first_name + '' + self.last_name

    def get_short_name(self):
        """Used to get users short name."""

        return self.first_name

    def ___str__(self):
        """Django uses this when it needs to convert the object to a string."""

        return self.email
