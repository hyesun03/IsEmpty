from django.db import models
from django.utils import timezone


class Room(models.Model):
    room_number = models.CharField(max_length=5)

    def __str__(self):
        return self.room_number + "호"


class Booking(models.Model):
    room = models.ForeignKey('Room')
    user = models.ForeignKey('accounts.User')

    book_date = models.DateField(default=timezone.now())
    start_time = models.TimeField(default=timezone.now())
    end_time = models.TimeField()

    purpose = models.CharField(max_length=50)
    participants = models.PositiveIntegerField()
