from django.db import models

# Create your models here.


class Match(models.Model):
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField()
    location = models.ForeignKey("Location", null=True, blank=True)
    homeTeam = models.ForeignKey("Teams")
    awayTeam = models.ForeignKey("Teams")

    manOfTheMatch = models.ForeignKey("Player", null=True, blank=True)
    bestGoal = models.ForeignKey("Player", null=True, blank=True)
    bestSave = models.ForeignKey("Player", null=True, blank=True)
    bestAssist = models.ForeignKey("Player", null=True, blank=True)


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
