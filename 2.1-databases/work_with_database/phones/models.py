from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    """Модель, представляющая собой телефон с полями для ввода
    идентификатора, названия, цены, URL-адреса изображения, дата выпуска,
    доступность LTE и slug. Включает в себя метод для возврата
    отформатированная строка названия, цены и даты выпуска.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self) -> str:
        """Возвращает отформатированную строку названия, цены и даты выпуска."""
        return f'{self.name} | {self.price} | {self.release_date}'

    def save(self, *args, **kwargs) -> None:
        """Генерирует slug при сохранении объекта.

        Данный метод переопределяет стандартный метод сохранения модели
        Django. Он устанавливает значение поля slug, если оно не было
        установлено ранее.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
