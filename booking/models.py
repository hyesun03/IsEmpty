from django.db import models
from django.utils import timezone


class Room(models.Model):
    room_number = models.CharField(max_length=5)

    def __str__(self):
        return self.room_number + "호"


class Booking(models.Model):
    HOURS = (
        ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'),
        ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')
    )
    MINUTES = (
        ('00', '00'), ('30', '30')
    )

    room = models.ForeignKey('Room')
    user = models.ForeignKey('accounts.User')

    is_delete = models.BooleanField(default=False)
    delete_date = models.DateTimeField(blank=True, null=True)

    book_date = models.DateField(default=timezone.now())
    start_hour = models.CharField(choices=HOURS, default='18', max_length=2)
    start_min = models.CharField(choices=MINUTES, default='00', max_length=2)
    end_hour = models.CharField(choices=HOURS, default='18', max_length=2)
    end_min = models.CharField(choices=MINUTES, default='00', max_length=2)

    purpose = models.CharField(max_length=50)
    participants = models.PositiveIntegerField()
