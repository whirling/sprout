from django.db import models
from django.utils import timezone


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    games = models.BooleanField(default=False)
    audio = models.BooleanField(default=False)
    affirmations = models.BooleanField(default=False)
    animals = models.BooleanField(default=False)
    c_visuals = models.BooleanField(default=False)
    hobbies = models.BooleanField(default=False)
    meditate = models.BooleanField(default=False)
    spaces = models.BooleanField(default=False)
    vent = models.BooleanField(default=False)
    visuals = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
