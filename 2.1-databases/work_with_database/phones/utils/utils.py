import csv


def get_sort_key(sort_by: str) -> str:
    """Возвращает ключ для сортировки телефонов.

    Возвращает ключ словаря сортировки, в случае если он существует,
    иначе возвращает ключ по умолчанию 'name'.

    Args:
        sort_by (str): Строка сортировки.

    Returns:
        str: Ключ для сортировки.
    """
    sort_columns = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    return sort_columns.get(sort_by, 'name')
