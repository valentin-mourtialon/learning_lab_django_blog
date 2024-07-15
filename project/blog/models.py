from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # For DateTimeField, the option auto_now=True would be great for a last_updated field.
    date_posted = models.DateTimeField(default=timezone.now)
    # If you delete a post, you're NOT going to delete the user.
    # If you delete the user, all related posts will also be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
