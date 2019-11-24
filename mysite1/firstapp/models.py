from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=200)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SignUP.objects.create(user=instance)

# @receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.SignUp.save()
