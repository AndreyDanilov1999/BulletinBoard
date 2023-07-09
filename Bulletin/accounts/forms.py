import random
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives, mail_managers


from accounts.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class ConfirmForm(forms.Form):
    confirm = forms.CharField(label='Code')
