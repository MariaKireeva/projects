from django.contrib import admin
from django.utils.html import format_html  # для отображения фото в админке
from .models import CustomUser


@admin.register(CustomUser)
class BoardAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 45px; height:45px;"/>'.format(obj.image.url))
    image_tag.short_description = 'изображение'


    list_display = ['username', 'email', 'avatar']