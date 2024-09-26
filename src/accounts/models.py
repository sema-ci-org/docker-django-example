from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name
