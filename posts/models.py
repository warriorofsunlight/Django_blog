from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    code = models.TextField(null=1, blank=1)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, models.CASCADE)
    attached_file = models.FileField(upload_to='files/',
                                     null=1, blank=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_author(self):
        return  (reverse('other',
                        kwargs={'author_pk':self.author.pk}))


