from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput

from .models import *


class FormPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',
                  'postCategory',
                  'file_image',
                  'file_video',
                  'file_audio',
                  ]
        labels = {
            'postCategory': 'Category',
            'file_image': 'Image',
            'file_video': 'Video',
            'file_audio': 'Audio',
        }


class FormFeedback(ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'text'
        ]

