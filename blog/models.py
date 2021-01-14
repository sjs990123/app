from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    #이미지 필드 추가
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} :: {}' .format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

class SearchList(models.Model):
    searchword = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searchword
