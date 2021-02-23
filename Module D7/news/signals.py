from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html
from .models import *
from .tasks import mail_new_post


@receiver(m2m_changed, sender=Post.post_category.through)
def notify_new_post(sender, instance, **kwargs):
    change_category = Category.objects.filter(postcategory__post=instance)
    if change_category.count() == 1:
        category = Category.objects.get(postcategory__post=instance)

        subscribers = User.objects.filter(categorysubscribers__category=category)
        email_subscribers = []
        for email in subscribers:
            email_subscribers.append(email.email)


        new_post = f'{instance.title}'
        link_id = instance.id
        link = f'http://127.0.0.1:8000/news/{link_id}'
        category = f'{category}'

        mail_new_post.apply_async([email_subscribers, new_post, link, category],countdown = 10)