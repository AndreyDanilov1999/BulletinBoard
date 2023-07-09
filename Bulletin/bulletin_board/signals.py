from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from Bulletin import settings
from .models import Feedback, Post


@receiver(post_save, sender=Feedback)
def feedback_is_create(created, sender, instance, **kwargs):
    if not created:
        return
    post = instance.feedbackPost.id
    post_name = instance.feedbackPost
    author_post = Post.objects.filter(id=post).values_list('author__username', 'author__email')
    for user, mail in author_post:
        html_content = render_to_string(
            'notifications/feedback_is_create.html',
            {
                'user': user,
                'post_name': post_name,
                'text': instance.text,
                'link': f'{settings.SITE_URL}/profile/'
            }
        )

        msg = EmailMultiAlternatives(
            subject='New feedback on the your Post',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            cc='',
            to=[mail]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@receiver(post_save, sender=Feedback)
def feedback_is_change(sender, instance, **kwargs):
    post = instance.feedbackPost.id
    post_name = instance.feedbackPost
    author = instance.author.username
    author_mail = instance.author.email
    if instance.status == 'Accept':
        html_content = render_to_string(
            'notifications/feedback_is_accept.html',
            {
                'user': author,
                'post_name': post_name,
                'text': instance.text,
                'link': f'{settings.SITE_URL}/posts/{post}/'
            }
        )

        msg = EmailMultiAlternatives(
            subject='New feedback on the your Post',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            cc='',
            to=[author_mail]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    elif instance.status == 'Reject':
        html_content = render_to_string(
            'notifications/feedback_is_reject.html',
            {
                'user': author,
                'post_name': post_name,
                'text': instance.text,
                'link': f'{settings.SITE_URL}/profile/'
            }
        )

        msg = EmailMultiAlternatives(
            subject='New feedback on the your Post',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            cc='',
            to=[author_mail]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    else:
        return