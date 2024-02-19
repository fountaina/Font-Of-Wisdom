from django.utils.text import Truncator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import itertools



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    snippet = models.CharField(default="", max_length=255)

    def get_snippet(self):
        # Truncate to desired word count
        words = self.body.split()
        return " ".join(itertools.islice(words, 0, 20)) + "..."  # Adjustable count
    
    def get_absolute_url(self):
        return reverse("home_page")


