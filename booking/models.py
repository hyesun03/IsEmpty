from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from utils.models import AliveManager


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

    book_date = models.DateField(default=timezone.now)
    start_hour = models.CharField(choices=HOURS, default='18', max_length=2)
    start_min = models.CharField(choices=MINUTES, default='00', max_length=2)
    end_hour = models.CharField(choices=HOURS, default='18', max_length=2)
    end_min = models.CharField(choices=MINUTES, default='00', max_length=2)

    purpose = models.CharField(max_length=50)
    participants = models.PositiveIntegerField()

    objects = models.Manager()
    alive_objects = AliveManager()

    def clean(self):
        if int(self.end_hour)*60 + int(self.end_min) <= int(self.start_hour)*60 + int(self.start_min):
            raise ValidationError(_('적절하지 않은 시간입니다.'))

        # 여기 부터는 기존 예약과 비교하는 로직
        date = self.book_date
        books = Booking.alive_objects.filter(book_date=date, room=self.room_id)

        if books:
            time_array = make_time_array(books)
            booking_validation(time_array, self)


def make_time_array(booking_objects):
    # 30개 크기의 배열을 만들고(9:00 - 24:00)
    # 배열은 30분 단위로 한 칸씩이다.
    time_array = []
    for i in range(30):
        time_array.append(0)

    # 해당되는 시간에 배열 색칠(1로 바꿈)
    for book in booking_objects:
        # 색칠할 범위 인덱스
        start_idx = (int(book.start_hour) - 9) * 2
        end_idx = (int(book.end_hour) - 9) * 2

        # min이 30이면 배열 한 칸 더 추가
        if (int(book.start_min) == 30):
            start_idx += 1
        if (int(book.end_min) == 30):
            end_idx += 1

        # start_idx에서 end_idx까지 색칠
        for i in range(start_idx, end_idx):
            time_array[i] = 1

    return time_array


def booking_validation(current_booking_array, new_booking):
    start_idx = (int(new_booking.start_hour) - 9) * 2
    end_idx = (int(new_booking.end_hour) - 9) * 2

    # min이 30이면 배열 한 칸 더 추가
    if (int(new_booking.start_min) == 30):
        start_idx += 1
    if (int(new_booking.end_min) == 30):
        end_idx += 1

    for i in range(start_idx, end_idx):
        if (current_booking_array[i] == 1):
            raise ValidationError(_('이미 예약되어있는 시간대 입니다.'))
