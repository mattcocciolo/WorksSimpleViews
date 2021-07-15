from django.db import models


# Create your models here.


class MusicalWorks(models.Model):
    title = models.CharField(max_length=250)
    contributors = models.CharField(max_length=350)
    iswc = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title
