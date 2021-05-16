from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import CustomUser
from django.forms import TextInput, PasswordInput, EmailInput, DateTimeInput, DateField
from django.forms import ModelForm
from django import forms

from django.forms.widgets import ClearableFileInput, FileInput

# Метод переопределяет форму регистрации через allauth. Достаем пользователя из реквест, достаем группу
# common через гет, в эту группу добавляем пользователя
class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        # Также создаем профиль для нового пользователя
        return user


# Форма редактирования профиля пользователя
class EditForm(ModelForm):
    avatar = forms.ImageField(label='Ваше фото', required=False, widget=FileInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth','email', 'avatar']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите логин'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ваше имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ваше имя'
            }),
            'date_of_birth': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата рождения"
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ваше имя'
            }),
        }


# Стандартный метод регистрации джанго. В данном проекте не используется
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите логин'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ваше имя'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'не менее 8 символов'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'повторите пароль'
            }),
        }