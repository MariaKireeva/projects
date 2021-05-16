from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'apps.posts'

    def ready(self):
        from apps.posts import signals