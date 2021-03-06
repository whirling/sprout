from django.db import models
from django.utils import timezone


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    # author = models.ForeignKey('auth.User')
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    # issue = models.TextField(default='')
    # wheelchair_accessible = models.BooleanField(default=False)
    # money = models.BooleanField(default=False)
    # parentalconsent = models.BooleanField(default=False)
    # min_age = models.TextField(default='0')
    # max_age = models.TextField(default='99')
    # transportation = models.BooleanField(default=False)
    # contact = models.EmailField(default='')
    chat = models.BooleanField(default=False)
    hotline = models.BooleanField(default=False)
    self_help = models.BooleanField(default=False)
    therapy = models.BooleanField(default=False)

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
