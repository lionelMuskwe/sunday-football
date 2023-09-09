from django.db import models

# Create your models here.
class Player(models.ModeL):
    firstName = models.CharField(max_length="100")
    lastName = models.CharField(max_length="100")
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
