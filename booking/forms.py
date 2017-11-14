from django import forms
from .models import Booking

class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'user', 'book_date', 'start_hour', 'start_min', 'end_hour', 'end_min', 'purpose',
                  'participants']

        labels = {
            'room': '강의실',
            'user': '예약자',
            'book_date': '예약일',
            'start_hour': '시',
            'start_min': '분 에서',
            'end_hour': '시',
            'end_min': '분 까지',
            'purpose': '이용목적',
            'participants': '이용자수'
        }
