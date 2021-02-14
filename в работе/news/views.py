from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post,Category,CategorySubscribers
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.conf import settings



class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_politic'] = Category.objects.get(category_name='Politics').id
        context['category_sport'] = Category.objects.get(category_name='Sport').id
        context['category_nature'] = Category.objects.get(category_name='Nature').id
        context['category_economics'] = Category.objects.get(category_name='Economics').id
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    form_class = PostForm
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        a = ''
        for i in Post.objects.get(pk=id).post_category.all().values('category_name'):
            a += (i['category_name'] + ' ')
        context['categories'] = a
        return context




    # дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('news.add_post','news.view_post')




class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    permission_required = ('news.change_post','news.view_post')


    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostSearchView(ListView):
    template_name = 'post_search.html'
    form_class = PostForm
    queryset = Post.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context

class PostCategory(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'PostCategory'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # Контекст для списка новостей в текущей категории
        context['category_news'] = Post.objects.filter(post_category=id)
        # Контекст подписан ли пользователь на текущую категорию. .exists() возвращает булево значение
        context['is_subscribe'] = CategorySubscribers.objects.filter(category=id, user=self.request.user).exists()
        return context


@login_required
def subscribe_category(request):
    # Достаем текущего пользователя
    user = request.user
    # Получаем ссылку из адресной строки и берем pk как id категории
    id = request.META.get('HTTP_REFERER')[-1]
    # Получаем текущую категорию
    category = Category.objects.get(id=id)
    print(id)
    # Создаем связь между пользователем и категорией
    category.subscribers.add(user)
    send_mail(
        subject=f'{User.username} ',
        # имя клиента и дата записи будут в теме для удобства
        message=f'Вы подписались на категорию {category}',  # сообщение с кратким описанием проблемы
        from_email=settings.DEFAULT_FROM_EMAIL,  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[f'{user.email}', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    )
    print(f'send email to {user.email}')
    return redirect('/')

@login_required
def unsubscribe_category(request):
    # Достаем текущего пользователя
    user = request.user
    # Получаем ссылку из адресной строки и берем pk как id категории
    id = request.META.get('HTTP_REFERER')[-1]
    # Получаем текущую категорию
    category = Category.objects.get(id=id)
    # Разрываем связь между пользователем и категорией
    category.subscribers.remove(user)
    send_mail(
        subject=f'{category.subscribers}',
        # имя клиента и дата записи будут в теме для удобства
        message=f'Вы отписались от категории {category}',  # сообщение с кратким описанием проблемы
        from_email=settings.DEFAULT_FROM_EMAIL,  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[f'{user.email}', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    )
    print(f'send email to {user.email}')
    return redirect('/')

