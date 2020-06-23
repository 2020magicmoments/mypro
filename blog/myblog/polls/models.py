from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=100)
    post_data = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='post/image', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.post_img.delete()
        super().delete(*args, **kwargs)
