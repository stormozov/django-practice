""" Модуль содержит класс для поиска предыдущей и следующей даты публикации
книги в базе данных."""
from books.models import Book


class DateFinder:
	"""Класс для поиска предыдущей и следующей даты публикации книги
	в базе данных"""
	def __init__(self, pub_date: str) -> None:
		"""Инициализирует дату публикации книги для поиска предыдущей и
		следующей даты публикации в базе данных"""
		self.pub_date = pub_date

	def find_prev_date(self) -> Book | None:
		""" Возвращает предыдущую дату, если она существует

		Return:
			Book: Запись книги из базы данных с предыдущей датой публикации
			None: Если предыдущей даты публикации не существует
		"""
		return (
			Book.objects
			.exclude(pub_date=self.pub_date)
			.filter(pub_date__lt=self.pub_date)
			.order_by('-pub_date')
			.first()
		)

	def find_next_date(self) -> Book | None:
		""" Возвращает следующую дату, если она существует

		Return:
			Book: Запись книги из базы данных со следующей датой публикации
			None: Если следующей даты публикации не существует
		"""
		return (
			Book.objects
			.exclude(pub_date=self.pub_date)
			.filter(pub_date__gt=self.pub_date)
			.order_by('pub_date')
			.first()
		)
