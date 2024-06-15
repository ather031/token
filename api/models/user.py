from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

def get_profile_image_path(self, filename):
    return f'profile_images/users/{self.pk}/{str(uuid.uuid4())}.png'


def get_default_profile_image_path():
    return f'profile_images/{"default_profile_image.png"}'

gender_choices = [('male', 'male'), ('female', 'female'), ('others', 'others')]

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None):
        if not username:
            raise ValueError('User must have a username.')
        if not first_name:
            raise ValueError('User must have a first name.')
        if not last_name:
            raise ValueError('User must have a last name.')
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username                = models.CharField(max_length=30, unique=True)
    first_name              = models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    full_name               = models.CharField(max_length=90, blank=True, null=True)
    is_staff                = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self,*args,**kwargs):
        self.full_name = self.first_name + " " + self.last_name
        return super().save(*args,**kwargs)