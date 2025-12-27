from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import EventBooking


class Registeruser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']


class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['event_date']
        widgets = {
            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'min': timezone.now().date()
            })
        }

    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']
        if event_date < timezone.now().date():
            raise forms.ValidationError("Past dates are not allowed.")
        return event_date
