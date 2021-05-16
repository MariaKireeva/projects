from django.db.models.signals import post_save, pre_save, m2m_changed, post_init
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from .models import Author, Post, Category
from django.template.loader import render_to_string
import time
from django.core.mail import send_mail
from  django.core.signals import request_finished

@receiver(m2m_changed, sender=Post.response.through)
def notify_response_accepted(sender, action, instance, **kwargs):
    if action == 'post_add':
        author_email = instance.author.author.email
        # user - тот, кто отправил отклик:
        user = instance.response.all().order_by('-id')[0]
        link_id = instance.id
        link = f'http://127.0.0.1:8000/posts/{link_id}'
        html_content = render_to_string(
            '../templates/posts/mail_response.html',
            {
                'author': instance.author.author.username, 'link': link, 'user': user, 'headline': instance.headline
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'{instance.headline}',
            from_email='markakireeva@yandex.ru',
            to= [author_email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

# отправление письмо юзеру, отклик которого приняли
@receiver(m2m_changed, sender=Post.accepted_response.through)
def notify_response_accepted(sender, action, instance, **kwargs):
    if action == 'post_add':
        author = instance.author.author.username
        # user - тот, кто отправил отклик:
        user = instance.accepted_response.all().order_by('-id')[0]
        link_id = instance.id
        link = f'http://127.0.0.1:8000/posts/{link_id}'
        html_content = render_to_string(
            '../templates/posts/accept_response.html',
            {
                'author': author, 'link': link, 'headline': instance.headline, 'user': user.username,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'{instance.headline}',
            from_email='markakireeva@yandex.ru',
            to= [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
