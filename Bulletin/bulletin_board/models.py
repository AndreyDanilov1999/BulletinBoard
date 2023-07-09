from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64, unique=True)
    text = models.TextField()
    file_image = models.ImageField(upload_to='images', blank=True, null=True)
    file_video = models.FileField(upload_to='video', blank=True, null=True)
    file_audio = models.FileField(upload_to='audio', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return str(self.title)

    def preview(self):
        return self.text[0:123] + '...'

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class Feedback(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feedbackPost = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    NOTVIEWED = 'NW'
    ACCEPT = 'AC'
    REJECT = 'RJ'
    STATUS_CHOICES = (
        (NOTVIEWED, 'Not Viewed'),
        (ACCEPT, 'Accept'),
        (REJECT, 'Reject'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='Not Viewed', max_length=128, verbose_name='status_feedback')

    def __str__(self):
        return str(self.text)


class FeedbackPost(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    feedbackThrough = models.ForeignKey(Feedback, on_delete=models.CASCADE)


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

