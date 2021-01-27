
from django.contrib.auth.models import User
from django.db import models




class Author(models.Model):
    author_raiting = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE, unique= True)

    def update_raiting(self):
        posts = Post.objects.filter(author = self.id)
        post_raiting = sum([r.post_raiting * 3 for r in posts]) # рейтинг каждого поста автора умножен на 3
        comment_raiting = sum([r.com_raiting for r in Comment.objects.filter(author=self.author)]) # сумма лайков/дислайков к комментам автора
        all_comment_raiting = sum([r.com_raiting for r in Comment.objects.filter(post__in = posts)]) # сумма лайков/дислайков всех комментов к постам автора
        self.author_raiting = post_raiting + comment_raiting + all_comment_raiting
        self.save()


    def __str__(self):
        return self.author.username

class Category(models.Model):
    topic = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'

    POST_TYPES = [
        (NEWS, 'News'),
        (ARTICLE, 'Article'),
    ]
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_raiting = models.IntegerField(default=0)
    type = models.CharField(max_length=2, choices = POST_TYPES, default = NEWS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')


    def like(self):
        self.post_raiting += 1
        self.save()

    def dislike(self):
        self.post_raiting -= 1
        self.save()

    def preview(self):
        preview = str(self.text)[:125] + "..."
        return preview


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    com_raiting = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.com_raiting += 1
        self.save()
    def dislike(self):
        self.com_raiting -= 1
        self.save()

    def __str__(self):
        info = str(self.author.username) + ' - ' + str(self.id)
        return info




