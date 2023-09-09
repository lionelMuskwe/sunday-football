from django.db import models

# Create your models here.
class Team(models.Model):
    player1 = models.ForeignKey("Player", null=True, blank=True)
    player2 = models.ForeignKey("Player", null=True, blank=True)
    player3 = models.ForeignKey("Player", null=True, blank=True)
    player4 = models.ForeignKey("Player", null=True, blank=True)
    player5 = models.ForeignKey("Player", null=True, blank=True)
    player6 = models.ForeignKey("Player", null=True, blank=True)
    player7 = models.ForeignKey("Player", null=True, blank=True)
    player8 = models.ForeignKey("Player", null=True, blank=True)
    player9 = models.ForeignKey("Player", null=True, blank=True)
    player10 = models.ForeignKey("Player", null=True, blank=True)
    player11 = models.ForeignKey("Player", null=True, blank=True)
    player12 = models.ForeignKey("Player", null=True, blank=True)
    player13 = models.ForeignKey("Player", null=True, blank=True)
    player14 = models.ForeignKey("Player", null=True, blank=True)
    player15 = models.ForeignKey("Player", null=True, blank=True)