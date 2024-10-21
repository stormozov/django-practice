"""Модуль для определения моделей."""
from django.db import models


class Article(models.Model):
    """Модель для статей.

    Поля:
        title (CharField): Название статьи.
        text (TextField): Текст статьи.
        published_at (DateTimeField): Дата публикации статьи.
        image (ImageField): Изображение статьи.
        article_scopes (ManyToManyField): Многие ко многим связь между статьями
            и тегами.
    """

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    article_scopes = models.ManyToManyField(
        'Tag',
        through='Scope',
        related_name='articles',
        verbose_name='Тематика статьи',
    )

    class Meta:
        """Определяет метаданные модели."""
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self) -> str:
        """Возвращает строковое представление модели."""
        return self.title


class Tag(models.Model):
    """Модель для тегов.

    Поля:
        name (CharField): Название тега.
    """

    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        """Определяет метаданные модели."""
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        """Возвращает строковое представление модели."""
        return self.name


class Scope(models.Model):
    """Модель для связи статьи и тега.

    Поля:
        article (ForeignKey): Статья.
        tag (ForeignKey): Тег.
        is_main (BooleanField): Основной ли тег.
    """

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='scopes',
    )
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        """Определяет метаданные модели."""
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self) -> str:
        """Возвращает строковое представление модели."""
        return f'{self.article} - {self.tag}'
