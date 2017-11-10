from django.contrib import admin

from accounts.models import *
from booking.models import *


admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(User)
