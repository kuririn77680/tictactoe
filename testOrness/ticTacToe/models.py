from django.db import models

# Create your models here.
class TicTacToe(models.Model):
    game_id = models.IntegerField(primary_key=True, auto_created=True)


class Cell(models.Model):
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    game = models.ForeignKey(TicTacToe, on_delete=models.CASCADE)
    value = models.CharField(null=False)