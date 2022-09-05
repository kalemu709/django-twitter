from django.db import models
from django.contrib.auth.models import User
from util import time_util


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def hours_age(self):
        return time_util.hours_to_now(self, self.created_at)

    def __str__(self):
        return 'tweet#' + self.id.__str__()
