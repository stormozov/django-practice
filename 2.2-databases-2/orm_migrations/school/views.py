"""Модуль, содержащий представления для школы."""
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Student


@cache_page(60 * 15)
def students_list(request):
    """Создает список студентов, упорядоченный по группам и именам.

    Аргументы:
        request (Request): Объект запроса Django.

    Возвращает:
        HttpResponse: Отрисованная HTML-страница со списком студентов.
    """
    template = 'school/students_list.html'
    students = (
        Student
        .objects
        .prefetch_related('teachers')
        .all()
        .order_by('group', 'name')
    )
    context = {
        'object_list': students,
    }

    return render(request, template, context)
