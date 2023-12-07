# fileshare_app/models.py
from django.db import models

class SharedFile(models.Model):
    pin = models.CharField(max_length=4, unique=True)
    file = models.FileField(upload_to='shared_files/')

    def __str__(self):
        return self.pin
