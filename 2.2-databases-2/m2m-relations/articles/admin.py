"""Модуль для регистрации моделей в админ-панели."""
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    """Переопределенная форма для связи статьи и тега."""

    def clean(self) -> None:
        """Проверка на то, что у статьи только один основной тег.

        Если у статьи больше одного основного тега, то в админ-панели будет
        выведено исключение и форма не будет сохранена.

        Исключение:
            ValidationError: Если у статьи больше одного основного тега.
        """
        main_scopes_count = sum(
            1
            for form in self.forms
            if form.cleaned_data.get('is_main')
        )

        if main_scopes_count > 1:
            raise ValidationError('Основной тег может быть только один.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    """Инлайн-форма для связи статьи и тега."""
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Регистрация модели статьи в админ-панели."""
    inlines = [ScopeInline]
    list_display = ['title', 'id', 'published_at']
    list_filter = ['published_at', 'article_scopes']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Регистрация модели тега в админ-панели."""
    list_display = ['name', 'id']
