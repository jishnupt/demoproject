from django.db import models

# Create your models here.

class MainEvents(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main events')

    def __str__(self):
        return self.title
    
