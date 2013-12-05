from django.db import models

# Create your models here.
class Meetup(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='meetup', blank=True)
    def __unicode__(self):
        return self.name
