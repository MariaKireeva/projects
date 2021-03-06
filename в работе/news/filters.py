from django_filters import FilterSet
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):

    class Meta:
        model = Post

        fields = {'title': ['icontains'],
                  'date': ['lt'],
                  'text': ['exact'],
                  'author': ['exact'],
                  'post_category': ['exact'],
                  'type': ['exact'],

                  }