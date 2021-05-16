from django.urls import path
from.views import PostList, AddProtectedView, PostDetail, MyPosts, Chats, MyChat, CreateChat, PostDeleteView, PostUpdateView, SearchList, TagList

urlpatterns =[
    path('', PostList.as_view(), name='post_list'),
    path('add/', AddProtectedView.as_view(), name='add_post'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('myposts', MyPosts.as_view(), name='my_posts'),
    path('messages/', Chats.as_view(), name='chats'),
    path('messages/<int:pk>', MyChat.as_view(), name='message'),
    path('makechat/<int:pk>', CreateChat.as_view(), name='make_chat'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search', SearchList.as_view(), name='search'),
    path('tag/<int:pk>', TagList.as_view(), name='taglist'),
]