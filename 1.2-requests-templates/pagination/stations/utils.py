"""Модуль, содержащий вспомогательные функции.

Функции:
    get_csv_data(): Возвращает список словарей с информацией о станциях.
    get_stations_info(): Генератор, который выдает словари с извлеченной
        информацией об автобусных станциях.
"""

import csv
from typing import Generator


def get_csv_data() -> list:
    """Возвращает список словарей с информацией о станциях."""
    with open('data-398-2018-08-30.csv', encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))


def get_stations_info(data: list) -> Generator:
    """Генератор, который выдает словари с извлеченной информацией
    об автобусных станциях.

    Args:
        data (list): Список словарей с информацией о станциях.

    Returns:
        Yields: Генератор словарей со следующими ключами:
            Name (str): Название автобусной остановки.
            Street (str): Улица автобусной остановки.
            District (str): Район автобусной остановки.
    """
    return ({
        'Name': station.get('Name'),
        'Street': station.get('Street'),
        'District': station.get('District')
    } for station in data)
