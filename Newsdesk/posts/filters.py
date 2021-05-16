from django_filters import FilterSet, MultipleChoiceFilter, ModelMultipleChoiceFilter, DateFromToRangeFilter, ChoiceFilter # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Category
from django_filters.widgets import RangeWidget, LookupChoiceWidget
from django.forms import ModelForm, ClearableFileInput, Textarea, Select, SelectMultiple, CheckboxSelectMultiple, ChoiceField



class PostFilter(FilterSet):
    create_time = DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))
    categories = ModelMultipleChoiceFilter( queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = {'headline': ['icontains'],
                  'author': ['exact'],
                  'categories': ['exact'],
                  }