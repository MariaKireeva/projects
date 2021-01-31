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
                  'categories': ['exact'],
                  'type': ['exact'],

                  }