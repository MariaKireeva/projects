from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True, default='avatar/default_user.png')
    date_of_birth = models.DateField(null=True, blank=True)
    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/mypage/'
    class Meta:
        db_table = 'auth_user'
"""    def save(self):
        super().save()
        avatar = Image.open(self.avatar.path)
        if avatar.height > 300 or avatar.width > 300:
            output_size = (300, 300)
            avatar.thumbnail(output_size)
            avatar.save(self.avatar.path)"""
