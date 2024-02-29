from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=10)
    image = models.ImageField(name=" ",width_field=500, height_field=500)