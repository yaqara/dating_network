from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class UserManager(UserManager):
    def create_user(self, email, password, is_superuser=False, is_staff=False, is_active=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = is_superuser
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, null=False, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    is_superuser = models.BooleanField(default=False)

    avatar = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()