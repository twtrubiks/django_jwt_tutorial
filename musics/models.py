from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"