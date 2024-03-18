from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking") 
    dateBooking = models.DateField()
    timeBooking = models.DateTimeField()
    numberBookig = models.IntegerField()
    notesBooking = models.TextField(max_length=500)

class TableDetails(models.Model):
    tableSize = models.IntegerField()    

class BookingDetails(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="bookingDetails") 
    tableId = models.ForeignKey(TableDetails, on_delete=models.CASCADE, related_name="bookingDetails") 


