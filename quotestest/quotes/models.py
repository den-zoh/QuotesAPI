from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quote(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_body = models.TextField()
    context = models.CharField(max_length=40)
    source = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote_author.username
