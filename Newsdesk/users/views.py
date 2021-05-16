from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from posts.models import Author, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import CustomUser
from .forms import EditForm
from posts.models import Post
from django.contrib import messages


class UserPage(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'mypage.html'
    login_url = '/mypage/login/'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        context['user'] = CustomUser.objects.get(username=user)
        category = Category.objects.filter(subscribers=user)
        # Блок для получения подписанных категории
        list_category = []
        for i in category:
            list_category.append(str(i))
        context['category'] = ', '.join(list_category)

        return context


@login_required
def upgrade_me(request):
    user = request.user
    print(user)
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(author=user)
    return redirect('/')


class EditProfile(LoginRequiredMixin, UpdateView):
    form_class = EditForm
    template_name = 'users/edit_profile.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return CustomUser.objects.get(pk=id)


