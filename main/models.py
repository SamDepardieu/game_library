from django.db import models


class GameType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Console(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.console.name})'
