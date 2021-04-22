from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BaseRegisterForm(SignupForm):

    def save(self, request):
        user = super(BaseRegisterForm, self).save(request)
        common_group = Group.objects.get(name='Common')
        common_group.user_set.add(user)
        return user





    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
