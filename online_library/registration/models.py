from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="user_avatar", default="image.png")
    books = models.ManyToManyField(Book, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "