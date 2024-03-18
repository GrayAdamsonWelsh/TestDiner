from django.contrib import admin
from .models import Booking
from .models import TableDetails
from .models import BookingDetails

# Register your models here.
admin.site.register(Booking)
admin.site.register(TableDetails)
admin.site.register(BookingDetails)
