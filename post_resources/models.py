from __future__ import unicode_literals

from django.db import models
from posts.models import Post
from resources.models import Resource
from django.contrib.auth.models import User
from utility.helpers import generate_str


class PostResource(models.Model):
    post = models.ForeignKey(
        Post,
        default='',
        on_delete=models.CASCADE
    )
    resource = models.ForeignKey(
        Resource,
        default='',
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=350,
        default=''
    )
    created_by = models.ForeignKey(
        User,
        default='',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return generate_str(
            [
                self.topic.name,
                self.description
            ]
        )
