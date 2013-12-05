from django.db import models


class Meetup(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='meetup_images', blank=True)
    def __unicode__(self):
        return self.name


# class Member(models.Model):
#     meetup = models.ForeignKey(Meetup)    
#     name = models.CharField(max_length=128, unique=False)
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#     website = models.URLField(blank=True)
#     def __unicode__(self):
#         return self.name
