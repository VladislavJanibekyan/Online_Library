from django.db import models
from django.contrib.auth.models import User
from languages.fields import LanguageField
GROUP_CHOICES = (
    (0, '0+'),
    (1, '7+'),
    (2, '13+'),
    (3, '18+')
)
# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=40)
    author = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=20)
    publish_year = models.IntegerField()
    language = LanguageField(max_length=40, default=False)
    age_group = models.IntegerField(choices=GROUP_CHOICES)
    downloaded_times = models.IntegerField()
    rate = models.FloatField()
    book_image = models.ImageField(upload_to='book_cover_image', default="image.png")
    pdf_file = models.FileField(default=True, upload_to='media')


    def __str__(self):
        return f"{self.title}|-|{self.category}|-|{self.author}"





