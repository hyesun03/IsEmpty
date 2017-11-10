from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, is_password_usable
from django.contrib.auth.models import UserManager
from utils.models import AliveManager


class User(AbstractUser):
    name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    is_admin = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    delete_date = models.DateTimeField(blank=True, null=True)

    objects = UserManager()
    alive_objects = AliveManager()


@receiver(pre_save, sender=User)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.password):
        instance.password = make_password(instance.password)
