from django.db import models
from django.utils import timezone


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    issue = models.TextField(default='')
    address = models.TextField(default='')
    accessibility = models.BooleanField(default=False)
    money = models.BooleanField(default=False)
    parentalconsent = models.BooleanField(default=False)
    age = models.TextField(default='')
    transportation = models.TextField(default='')
    openingTime = models.BooleanField(default=False)
    closingTime = models.BooleanField(default=False)
    contact = models.TextField(default='')
    insurance = models.BooleanField(default=False)
    hotline = models.TextField(default='')
    self_health = models.BooleanField(default=False)
    therapy = models.BooleanField(default=False)
    games = models.BooleanField(default=False)
    sounds = models.BooleanField(default=False)

#####
# soundList = {"noises": "relaxing_noises", }
########


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
