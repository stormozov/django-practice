"""Модуль содержит модели школы."""
from django.db import models


class Teacher(models.Model):
    """Представляет учителя в школе.

    Атрибуты:
        name (str): Имя учителя.
        subject (str): Предмет, преподаваемый учителем.

    Возвращает:
        str: Имя учителя в виде строкового представления.
    """
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        """Метаданные для модели Teacher.

        Атрибуты:
            verbose_name (str): Единственное имя для модели.
            verbose_name_plural (str): Множественное имя для модели.
        """
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self) -> str:
        """Возвращает строковое представление учителя.

        Возвращает:
            str: Имя учителя.
        """
        return self.name


class Student(models.Model):
    """Представляет ученика в школе.

    Атрибуты:
        name (str): Имя ученика.
        teachers (ManyToManyField): Преподаватели, назначенные ученику.
        group (str): Класс ученика.

    Возвращает:
        str: Имя ученика в виде строкового представления.
    """
    name = models.CharField(max_length=30, verbose_name='Имя')
    teachers = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        """Метаданные для модели Student.

        Атрибуты:
            verbose_name (str): Единственное имя для модели.
            verbose_name_plural (str): Множественное имя для модели.
        """
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self) -> str:
        """Возвращает строковое представление ученика.

        Возвращает:
            str: Имя ученика.
        """
        return self.name
