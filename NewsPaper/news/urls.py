from django.urls import path
from .views import NewsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView


urlpatterns = [

    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
    path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('search/', PostSearchView.as_view(), name='post_search'),

]