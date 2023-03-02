from django.db import models
from datetime import datetime
# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title