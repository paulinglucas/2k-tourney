from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profit(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=100, blank=True)
    last_name = models.CharField("Last Name", max_length=100, blank=True)
    email = models.EmailField("Email", max_length=150)
    current_profit = models.DecimalField("Current Profit", max_digits=10000, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
