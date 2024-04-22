from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=255)


class Game(models.Model):
    member_model = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)

    game_word_model = models.CharField(max_length=200)
    current_string_model = models.CharField(max_length=200)
    mistakes_model = models.IntegerField()
