from django.db import models


class GameType(models.Model):
    name = models.CharField(max_length=256)


class Console(models.Model):
    name = models.CharField(max_length=255)


class Game(models.Model):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
