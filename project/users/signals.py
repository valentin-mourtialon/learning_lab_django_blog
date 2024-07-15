from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a User is saved ...
# ... then send this signal "post_save" ...
# ... and this signal is going to be received by the "receiver" ...
# ... and this receiver is this "create_profile" function ...
# ... and this "create_profile" function takes all of these arguments that our "post_save" signal passed to it.
# One of those args is the instance of the user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
