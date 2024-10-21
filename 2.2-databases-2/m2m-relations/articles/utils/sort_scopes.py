"""Сортирует теги по is_main."""
from articles.models import Article


def sort_scopes(article: Article) -> list:
    """Сортирует теги для каждой статьи по is_main.

    Если тег основной, то он будет отсортирован первым в списке. Для сортировки
    используется метод sorted и lambda-функция.

    Args:
        article (Article): Объект статьи.

    Returns:
        list: Список тегов для каждой статьи.
    """
    return sorted(
        article.scopes.all(),
        key=lambda x: x.is_main,
        reverse=True
    )
