from django.shortcuts import render, redirect

from phones.models import Phone
from phones.utils.utils import get_sort_key


def index(request):
    """Перенаправление на шаблон URL 'catalog'.

    Args:
        request: Объект запроса.

    Returns:
        django.http.response.HttpResponseRedirect: Ответ на перенаправление.
    """
    return redirect('catalog')


def show_catalog(request):
    """Отображает список всех телефонов в каталоге.

    Сортирует телефоны по названию, цене или дате выпуска в зависимости от
    параметра 'sort' в строке запроса.

    Args:
        request: Объект запроса.

    Returns:
        django.http.response.HttpResponse: Ответ на запрос.
    """
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    phones = Phone.objects.order_by(get_sort_key(sort_by))
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug: str):
    """Отображает информацию о конкретном телефоне.

    Args:
        request: Объект запроса.
        slug (str): Идентификатор телефона.

    Returns:
        django.http.response.HttpResponse: Ответ на запрос.
    """
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}

    return render(request, template, context)
