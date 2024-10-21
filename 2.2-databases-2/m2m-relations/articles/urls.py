"""Настройка URL-адресов для приложения articles."""
from django.urls import path

from articles.views import (
    articles_list,
    article_details,
    tag_page,
    tag_page_main
)

urlpatterns = [
    # URL для работы со списком статей
    path('', articles_list, name='articles'),
    # URL для работы со страницей самой статьи
    path('<int:article_id>/', article_details, name='article_details'),
    # URL для работы с тегами
    path('tag/', tag_page_main, name='articles_by_tag'),
    path('tag/<int:tag_id>/', tag_page, name='articles_by_tag'),
    path(
        'tag/<int:tag_id>/<int:article_id>/',
        article_details,
        name='article_details'
    ),
]
