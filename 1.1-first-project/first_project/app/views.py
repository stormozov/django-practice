import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse

from app.data import header


def previous_page(request):
    return redirect('/')


def home_view(request):
    """ Домашняя страница """
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages,
        'page_title': 'Домашняя страница',
        'header': header,
    }

    return render(request, template_name, context)


def time_view(request):
    """ Возвращает текущее время """
    template_name = 'app/time.html'
    context = {
        'current_time': datetime.now(),
        'page_title': 'Текущее время',
        'header': header
    }

    return render(request, template_name, context)


def workdir_view(request):
    """ Возвращает список файлов в рабочей директории """
    template_name = 'app/workdir.html'
    context = {
        'files': os.listdir(),
        'page_title': 'Список файлов в рабочей директории',
        'header': header
    }

    return render(request, template_name, context)
