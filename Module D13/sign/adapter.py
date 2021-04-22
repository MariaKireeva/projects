from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter, get_account_adapter
from django.contrib.auth.models import Group
from django.conf import settings



class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = '/news'
        return path.format(username=request.user.username)

    def get_signup_redirect_url(self, request):
        path = '/news'
        return path



class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        u = super(SocialAccountAdapter,self).save_user(request, sociallogin, form=None)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(u)
        return u



