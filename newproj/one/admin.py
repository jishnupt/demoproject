from django.contrib import admin
from .models import MainEvents,Events,EventBooking

# Register your models here.

admin.site.register(MainEvents)
admin.site.register(Events)
admin.site.register(EventBooking)
