from django.db import models
from django.utils import timezone


class Resource(models.Model):
    issue = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    accessibility = models.BooleanField()
    money = models.BooleanField()
    parentalconsent = models.TextField()
    age = models.TextField()
    transportation = models.TextField()
    openingTime = models.BooleanField()
    closingTime = models.BooleanField()
    contact = models.TextField()
    insurance = models.BooleanField()



    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
