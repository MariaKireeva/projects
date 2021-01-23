from django.urls import path
from .views import NewsList, OnePost

urlpatterns = [

    path('', NewsList.as_view()),
    path('<int:pk>', OnePost.as_view()),
]