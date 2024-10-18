"""Администрирование моделей."""
from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Администрирование модели Student.

    Атрибуты:
        list_display (list): Поля, которые будут отображаться на странице
            списка.
        list_filter (list): Поля, по которым можно фильтровать список.
    """
    list_display = ['name', 'group']
    list_filter = ['group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Администрирование модели Teacher.

    Атрибуты:
        list_display (list): Поля, которые будут отображаться на странице
            списка.
        list_filter (list): Поля, по которым можно фильтровать список.
    """
    list_display = ['name', 'subject']
    list_filter = ['subject']
