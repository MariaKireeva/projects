from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from django.template.loader import render_to_string
from news.models import Post
from django.core.mail import mail_admins, send_mail


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'post_create.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Post(
            text_title=request.POST['title'],
            text_news=request.POST['text'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.title}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.text,  # сообщение с кратким описанием проблемы
            from_email='kireeva.mary2015@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=['mary5@list.ru']  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        return redirect('')
