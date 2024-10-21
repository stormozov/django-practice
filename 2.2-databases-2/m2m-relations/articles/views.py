"""Представления для приложения articles."""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from articles.models import Article, Tag
from articles.utils.sort_scopes import sort_scopes


def articles_list(request):
    """Views-функция для отображения списка статей.

    Она сортирует теги для каждой статьи по is_main (основной или нет) и
    добавляет их в дополнительное свойство sorted_scopes. Если тег основной,
    то он будет первым в списке. Затем она передает список статей в шаблон
    articles/news_details.html.

    Args:
        request: Объект запроса.

    Returns:
        HttpResponse: Ответ на запрос.
    """
    template = 'articles/news.html'
    articles = Article.objects.all()

    for article in articles:
        article.sorted_scopes = sort_scopes(article)

    return render(request, template, {'articles': articles})


def article_details(request, article_id: int, tag_id: int = None):
    """Views-функция для отображения детальной информации о статье.

    Args:
        request: Объект запроса.
        article_id (int): Идентификатор статьи.
        tag_id (int): Идентификатор основного тега статьи.

    Returns:
        HttpResponse: Ответ на запрос.
    """
    template = 'article_details/news_details.html'
    article = get_object_or_404(Article, id=article_id)

    article.sorted_scopes = sort_scopes(article)

    return render(request, template, {'article': article})


def tag_page_main(request):
    """Views-функция для перенаправления на страницу со списком статей."""
    return redirect(reverse('articles'))


def tag_page(request, tag_id: int):
    """Views-функция для отображения статей по тегу.

    Args:
        request: Объект запроса.
        tag_id (int): Идентификатор тега.

    Returns:
        HttpResponse: Ответ на запрос.
    """
    template = 'tag/tag.html'
    articles = Article.objects.filter(scopes__tag_id=tag_id)
    tag = get_object_or_404(Tag, id=tag_id)

    for article in articles:
        article.sorted_scopes = sort_scopes(article)

    context = {'articles': articles, 'tag': tag}

    return render(request, template, context)
