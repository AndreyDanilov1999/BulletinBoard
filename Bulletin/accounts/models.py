from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    code_of_confirm = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return str(self.code_of_confirm)
