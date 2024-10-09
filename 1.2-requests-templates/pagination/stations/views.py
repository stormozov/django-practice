from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from stations.utils import get_csv_data, get_stations_info


def index() -> render:
    """Возвращает шаблон index.html."""
    return redirect(reverse('bus_stations'))


def bus_stations(request) -> render:
    """Возвращает шаблон index.html с данными о станциях."""
    csv_data: list[dict] = get_csv_data()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list(get_stations_info(csv_data)), 10)
    page = paginator.page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
