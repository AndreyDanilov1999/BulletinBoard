import random
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, FormView

from Bulletin import settings
from .forms import SignUpForm, ConfirmForm
from .models import Profile


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/confirm'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        code = random.randint(1000, 9999)
        print(code)
        user.save()
        profile = Profile.objects.create(user=user, code_of_confirm=code)
        profile.save()
        send_mail(
            f"Добро пожаловать на наш сайт!",
            f'Поздравляем, {user.username}, ваша регистрация почти завершена. '
            f'Введите код {code} в форму на сайте, для подтверждения почты. '
            f'Ссылка для ввода кода: http://127.0.0.1:8000/accounts/confirm/',
            f"{settings.SERVER_EMAIL}",
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class ConfirmUser(FormView):
    model = Profile
    form_class = ConfirmForm
    success_url = '/accounts/login'
    template_name = 'registration/confirm.html'

    def form_valid(self, form):
        code = str(form.cleaned_data['confirm'])
        print(code)
        profile = Profile.objects.filter(code_of_confirm=code).values_list('code_of_confirm', flat=True)
        print(profile)
        us_id = list(Profile.objects.filter(code_of_confirm=code).values_list('user', flat=True))
        if profile.exists():
            user = User.objects.get(id=''.join(map(str, us_id)))
            user.is_active = True
            user.save()
            group = Group.objects.get(name='Authors')
            user.groups.add(group)
            return super().form_valid(form)
        else:
            message = loader.get_template('incorrect_input.html')
            return HttpResponse(message.render())












