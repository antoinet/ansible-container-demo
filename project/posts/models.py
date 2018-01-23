from django.db import models
from project.authentication.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)