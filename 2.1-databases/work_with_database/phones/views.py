from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render

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

    # Проверяем, есть ли в кэше сортированный список телефонов
    phones = cache.get('sorted_phones_%s' % sort_by)
    if phones is None:
        # Если нет, получаем список телефонов из базы данных и кэшируем его
        phones = Phone.objects.order_by(get_sort_key(sort_by))
        cache.set('sorted_phones_%s' % sort_by, phones, timeout=300)

    return render(request, template, {'phones': phones})


def show_product(request, slug: str):
    """Отображает информацию о конкретном телефоне.

    Args:
        request: Объект запроса.
        slug (str): Идентификатор телефона.

    Returns:
        django.http.response.HttpResponse: Ответ на запрос.
        django.shortcuts.get_object_or_404: Ошибка 404, если телефон не найден.
    """
    template = 'product.html'

    # Проверяем, есть ли в кэше информация о телефоне
    phone = cache.get('phone_%s' % slug)
    if phone is None:
        # Если нет, получаем информацию о телефоне из базы данных и кэшируем ее
        phone = get_object_or_404(Phone, slug=slug)
        cache.set('phone_%s' % slug, phone, timeout=300)

    return render(request, template, {'phone': phone})
