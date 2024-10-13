import csv

from django.core.management.base import BaseCommand

from main.settings import PHONES_CSV
from phones.models import Phone


class Command(BaseCommand):
    """Команда для импорта данных из CSV-файла в базу данных."""
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options) -> None:
        """Импортирует данные из CSV-файла в базу данных."""
        phones: list[dict] = self._get_data_from_csv(PHONES_CSV)
        for phone in phones:
            try:
                self._save_data_in_db(phone)
            except Exception as e:
                print(f'При импорте данных в базу данных произошла ошибка: {e}')

    def _save_data_in_db(self, phone: dict) -> None:
        """Сохраняет данные в базу данных.

        Если телефон с таким идентификатором уже существует в базе данных, то
        он обновляется. Если телефон с таким идентификатором не существует в
        базе данных, то он добавляется.

        Args:
            phone: словарь с данными о телефоне.
        """
        phone_obj, created = Phone.objects.get_or_create(
            id=phone['id'], defaults=phone
        )
        action = 'добавлен в базу' if created else 'обновлен в базе'
        print(
            f'"{phone["name"]}, {phone["price"]}₽, {phone["release_date"]}"'
            f' — {action} данными из CSV-файла'
        )
        if not created:
            self._update_existing_phone(phone_obj, phone)

    @staticmethod
    def _update_existing_phone(phone_obj: Phone, phone: dict) -> None:
        """Обновляет существующую запись телефона в базе данных."""
        for key, value in phone.items():
            setattr(phone_obj, key, value)
        phone_obj.save()

    @staticmethod
    def _get_data_from_csv(
            path: str, encoding: str = 'utf-8', delimiter: str = ';'
    ) -> list[dict]:
        """Возвращает список словарей, каждый из которых представляет телефон.

        Ожидается, что CSV-файл будет иметь следующую структуру:

        id;name;price;release_date;lte_exists
        1;Phone 1;1000;2019-01-01;True
        2;Phone 2;2000;2019-01-02;False

        Функция открывает CSV-файл, считывает его содержимое и возвращает
        список словарей, каждый из которых представляет телефон. Ключами
        словаря являются 'id', 'name', 'price', 'release_date' и
        'lte_exists', а значениями словаря - значения соответствующих
        столбцов в CSV-файле.

        Args:
            path (str): Путь к CSV-файлу.
            encoding (str, optional): Кодировка CSV-файла. По умолчанию 'utf-8'.
            delimiter (str, optional): Разделитель CSV-файла. По умолчанию ';'.

        Returns:
            list[dict]: Список словарей, каждый из которых представляет телефон.
        """
        with open(path, 'r', encoding=encoding) as file:
            return list(csv.DictReader(file, delimiter=delimiter))
