from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from accounts.models import Profile


@receiver(signal=user_logged_in)
def is_login(user, **kwargs):
    profile_id = list(Profile.objects.filter(user_id=user.id).values_list('user_id', flat=True))
    profile_list = ''.join(map(str, profile_id))
    if str(user.id) == profile_list:
        profile = Profile.objects.get(user=user.id)
        profile.delete()
    else:
        return
