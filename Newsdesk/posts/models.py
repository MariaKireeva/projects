from django.db import models
from Newsdesk.settings import AUTH_USER_MODEL
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='authors')
    def __str__(self):
        return f'{self.author}'
class Category(models.Model):
    tag = models.CharField(max_length= 100, unique=True)
    subscribers = models.ManyToManyField(AUTH_USER_MODEL, blank= True, null= True,
                                    related_name='subscribers',
                                    verbose_name='subscribers')

    def __str__(self):
        return f'{self.tag}'

class PostPhoto(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор", default= None)
    headline = models.CharField(max_length = 255, verbose_name= 'Заголовок', default= None)
    image = models.ImageField(upload_to='files', blank=True, null=True, default= None)
    categories = models.ManyToManyField(Category, verbose_name='категории', default= None)
    text = models.TextField(default=None)
    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/'
    class Meta:
        verbose_name_plural  = "фото"
class Post(models.Model):
    class Meta:
        verbose_name_plural  = "Объявления"

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    headline = models.CharField(max_length = 255, verbose_name= 'Заголовок')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField()
    categories = models.ManyToManyField(Category, verbose_name='категории',
                                        related_name='categories', help_text='tag')
    rating_of_post = models.IntegerField(default=0)
    likers = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                    related_name='likers',
                                    verbose_name='Понравилось')
    dislikers = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                       related_name='dislikers',
                                       verbose_name='Не понравилось')
    images = models.ManyToManyField(PostPhoto, blank=True, null=True,
                                    related_name='images')

    response = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                       related_name='response',
                                       verbose_name='отклики')
    accepted_response = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                       related_name='accepted',
                                       verbose_name='принятые')

    def like(self):
        self.rating_of_post += 1
        self.save()

    def dislike(self):
        self.rating_of_post -= 1
        self.save()
    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/{self.id}'

class Chat(models.Model):
    user1 = models.OneToOneField(AUTH_USER_MODEL, default= None, on_delete= models.CASCADE, verbose_name='user1', related_name = 'user1')
    user2 = models.OneToOneField(AUTH_USER_MODEL, default= None, on_delete= models.CASCADE, verbose_name='user2', related_name = 'user2')
    created = models.DateTimeField(auto_now_add=True)
class Message(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE, verbose_name='users')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500) # what length you want


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_user = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE)
    com_text = models.TextField(verbose_name='Text', help_text='comment')
    com_time = models.DateTimeField(default=timezone.now,)
    com_rating = models.IntegerField(default=0)
    com_likers = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                    related_name='com_likers',
                                    verbose_name='Понравилось')
    com_dislikers = models.ManyToManyField(AUTH_USER_MODEL, blank=True, null=True,
                                       related_name='com_dislikers',
                                       verbose_name='Не понравилось')

    def like(self):
        self.com_rating += 1
        self.save()
    def dislike(self):
        self.com_rating -= 1
        self.save()
    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/{self.comment_post.id}'

class Photo(models.Model):
    image = models.FileField(upload_to='files', blank=True, null=True)
