from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Chat, Comment, Category, Author, Message, PostPhoto
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm, CategoryForm, AddCommentForm, AddMessageForm, PhotoForm
from django.utils import timezone, dateformat
from datetime import datetime
import pytz
from itertools import chain
from users.models import CustomUser
from .filters import PostFilter
from django.http import HttpResponse
from django.views import View



class PostList(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formatted_date = dateformat.format(timezone.now(), 'Y-B-D H:i:s')
        fmt = '%d/%M/%Y %H:%M'
        utc = datetime.utcnow().replace(tzinfo=pytz.UTC)
        localtz = utc.astimezone(timezone.get_current_timezone())
        context['time_now'] = timezone.localtime(timezone.now())
        context['hour_now'] = ''
        context['form'] = PostForm()
        context[ 'timezones'] = pytz.common_timezones
        return context

class AddProtectedView(PermissionRequiredMixin, CreateView):
    template_name = 'posts/add_post.html'
    form_class = PhotoForm
    login_url='/accounts/login'
    permission_required = 'posts.add_post'
    model = PhotoForm
    queryset = Post.objects.all()


    def form_valid(self, form):
        self.object = form.save(commit= False)
        author = self.request.user
        id = Author.objects.get(author= author).id
        self.object.author_id = id
        self.object.save()
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        new_post = Post.objects.create(author= Author.objects.get(author =self.request.user), headline= self.request.POST['headline'], text= self.request.POST['text'])
        for tag in self.request.POST.getlist('categories'):
            new_post.categories.add(int(tag))
        images = self.request.FILES.getlist('images')
        print(self.request.FILES)
        for f in self.request.FILES.getlist('image'):
            print(f)
            newphoto = PostPhoto.objects.create(author= Author.objects.get(author =self.request.user), headline= self.request.POST['headline'], text= self.request.POST['text'], image= f)
            new_post.images.add(newphoto)
        return redirect(f'/posts/')

class PostDetail(CreateView):
    model = Comment
    template_name = 'posts/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
    form_class = AddCommentForm

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        user = self.request.user
        if str(user) is 'AnonymousUser':
            return redirect(f'/mypage/login/')
        else:
            if 'like_com' in self.request.POST.keys():
                pk = self.request.POST['like_com']
                Comment.objects.get(pk=pk).like()
                Comment.objects.get(pk=pk).com_likers.add(user)
            elif 'dislike_com' in self.request.POST.keys():
                pk = self.request.POST['dislike_com']
                Comment.objects.get(pk=pk).dislike()
                Comment.objects.get(pk=pk).com_dislikers.add(user)
            elif 'like_post' in self.request.POST.keys():
                Post.objects.get(pk=id).like()
                Post.objects.get(pk=id).likers.add(user)
            elif 'dislike_post' in self.request.POST.keys():
                Post.objects.get(pk=id).dislike()
                Post.objects.get(pk=id).dislikers.add(user)
            elif "subscribe" in self.request.POST.keys():
                pk = self.request.POST['subscribe']
                Category.objects.get(pk=pk).subscribers.add(user)
            elif "unsubscribe" in self.request.POST.keys():
                pk = self.request.POST['unsubscribe']
                Category.objects.get(pk=pk).subscribers.remove(user)
            elif "com_text" in self.request.POST.keys():
                text = self.request.POST['com_text']
                Comment.objects.create(comment_user=user, comment_post = Post.objects.get(pk = id), com_text= text)
            elif "response" in self.request.POST.keys():
                Post.objects.get(pk=id).response.add(user)
            return redirect(f'/posts/{id}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        user = self.request.user
        if str(user) is 'AnonymousUser':
            context['post'] = Post.objects.get(pk=id)
            context['post_categories'] = Post.objects.get(pk=id).categories.all()
            context['rating'] = Post.objects.get(pk=id).rating_of_post
            context['comments'] = Comment.objects.filter(comment_post=Post.objects.get(pk=id))
            context['likers'] = Post.objects.get(pk=id).likers.all()
            context['dislikers'] = Post.objects.get(pk=id).dislikers.all()
            context['all_tags'] = Category.objects.all()
            return context
        else:
            context['post'] = Post.objects.get(pk=id)
            context['post_categories'] = Post.objects.get(pk=id).categories.all()
            context['user_categories'] = Category.objects.filter(subscribers= user)
            context['rating'] = Post.objects.get(pk=id).rating_of_post
            context['comments'] = Comment.objects.filter(comment_post=Post.objects.get(pk=id))
            context['likers'] = Post.objects.get(pk=id).likers.all()
            context['dislikers'] = Post.objects.get(pk=id).dislikers.all()
            context['all_tags'] = Category.objects.all()
            context['images'] = Post.objects.get(pk=id).images.all()
            return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        id = self.kwargs.get('pk')
        user = self.request.user
        self.object.comment_user = user
        self.object.comment_post_id = id
        self.object.save()
        return super().form_valid(form)

class MyPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/my_posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_posts'] = Post.objects.filter(author= Author.objects.get(author = user))
        return context

    def post(self, request, *args, **kwargs):
        if 'accept_response' in self.request.POST.keys():
            a = str(self.request.POST['accept_response']).split(' ')
            post = Post.objects.get(pk=int(a[0]))
            post.accepted_response.add(a[1])
            post.response.remove(a[1])
        elif 'delete_response' in self.request.POST.keys():
            a = str(self.request.POST['delete_response']).split(' ')
            post = Post.objects.get(pk= int(a[0]))
            post.response.remove(a[1])
        return redirect(f'/posts/myposts')

class Chats(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'posts/chats.html'
    context_object_name = 'messages'
    queryset = Chat.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_chats']  = list(chain(Chat.objects.filter(user1= user.id), Chat.objects.filter(user2= user.id)))
        return context

class MyChat(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'posts/message.html'
    form_class = AddMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        id = self.kwargs.get('pk')

        context['users'] = Chat.objects.get(pk = id)
        if user == context['users'].user1:
            context['companion'] = context['users'].user2
        else:
            context['companion'] = context['users'].user1
        context['messages'] = Message.objects.filter(chat= id).order_by('-id')
        return context

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        if "text" in self.request.POST.keys():
            text = self.request.POST['text']
            user = self.request.user
            Message.objects.create(user=user, chat = Chat.objects.get(pk = id), text= text)
        return redirect(f'/posts/messages/{id}')

class CreateChat(ListView):
    template_name = 'posts/create_chat.html'
    model = CustomUser
    queryset = CustomUser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user1 = self.request.user
        id = self.kwargs.get('pk')
        user2 = CustomUser.objects.get(pk= id)
        context['user2'] = user2
        if Chat.objects.filter(user1= user1, user2=user2) or Chat.objects.filter(user1= user2, user2=user1):
            context['chat'] = True
        else:
            context['chat'] = False
        return context
    def post(self, request, *args, **kwargs):
        user1 = self.request.user
        id = self.kwargs.get('pk')
        user2 = CustomUser.objects.get(pk= id)
        Chat.objects.create(user1= user1, user2= user2)
        return redirect(f'/posts/messages/')

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'posts/add_post.html'
    form_class = PostForm
    permission_required = ('posts.change_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'posts/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
    permission_required = ('posts.delete_post')

class SearchList(ListView):
    model = Post
    template_name = 'posts/search.html'
    context_object_name = 'posts'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class TagList(ListView):
    model = Post
    template_name = 'posts/tag_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['time_now'] = timezone.localtime(timezone.now())
        context['tag_post'] = Post.objects.filter(categories= id)
        return context
