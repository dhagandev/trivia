from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    q_correct = models.IntegerField(default=0)
    q_answered = models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.user.id})

class Question(models.Model):
    category = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    q_text = models.TextField()
    correct_ans = models.TextField()
    incorrect_ans = ArrayField(models.TextField())

    def get_absolute_url(self):
        return reverse('question_display', kwargs={'question_id': self.id})
