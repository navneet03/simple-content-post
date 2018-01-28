from __future__ import unicode_literals
from django.db import models
from accounts.models import User


class ContentPost(models.Model):
    """
    Model that represents an Content Post data.
    """
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_posts')

    title = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField(blank=True, null=True)

    publish = models.DateTimeField(blank=True, null=True)

    likes = models.ManyToManyField(User, related_name='likes', null=True, blank=True)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ('-publish',)

