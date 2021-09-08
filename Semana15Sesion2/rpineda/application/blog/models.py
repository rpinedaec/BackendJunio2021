from django.db import models

import uuid

class Author(models.Model):
    id = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
class Post(models.Model):
    id = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
class Tag(models.Model):
    id = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
