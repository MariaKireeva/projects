from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
    path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('category/<int:pk>', PostCategory.as_view(), name='category'),
    path('category/subscribe/', subscribe_category, name='subscribe'),
    path('category/unsubscribe/', unsubscribe_category, name='unsubscribe'),

]