from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post,Category
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime



class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
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
        for i in Post.objects.get(pk=id).categories.all().values('topic'):
            a += (i['topic'] + ' ')
        context['categories'] = a
        return context




    # дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm



class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()


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











