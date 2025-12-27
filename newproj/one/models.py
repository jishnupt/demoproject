from django.db import models

# Create your models here.

class MainEvents(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main events')

    def __str__(self):
        return self.title
    
class Events(models.Model):
    E_name = models.CharField(max_length=50)
    location = models.TextField(null=True)
    main_event = models.ForeignKey(MainEvents,on_delete=models.CASCADE)
    E_image = models.ImageField(upload_to='events')

    def __str__(self):
        return self.E_name


class EventBooking(models.Model):
    name = models.OneToOneField(Events,on_delete=models.CASCADE)
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    
