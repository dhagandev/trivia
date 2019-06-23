from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	q_correct = models.IntegerField()
	q_answered = models.IntegerField()

class Question(models.Model):
	category = models.CharField(max_length=200)
	difficulty = models.CharField(max_length=50)
	q_text = models.TextField()
	correct_ans = models.TextField()
	incorrect_ans = ArrayField(models.TextField())