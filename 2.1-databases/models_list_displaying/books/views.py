from audioop import reverse

from django.shortcuts import redirect, render
from django.urls import reverse

from books.converters import DateConverter
from books.date_finder import DateFinder
from books.models import Book


def index(request):
    """Перенаправляет на страницу каталога."""
    return redirect(reverse('books_list'))


def books_list(request):
    """Возвращает страницу со списком книг.

    Для каждой книги в базе данных формирует url,
    который будет использоваться для перехода
    к подробному описанию книги.
    """
    all_books = Book.objects.all()

    for book in all_books:
        pub_date_filter = DateConverter().to_python(str(book.pub_date))
        book.slug = DateConverter().to_url(pub_date_filter)

    return render(request, 'books/books_list.html', {'books': all_books})


def books_details(request, pub_date):
    """Возвращает страницу с выбранной книгой.

    Формирует url для предыдущей и следующей даты публикации книги.
    """
    selected_books = Book.objects.filter(pub_date=pub_date)
    date_finder = DateFinder(pub_date)
    previous_book = date_finder.find_prev_date()
    next_book = date_finder.find_next_date()

    return render(request, 'books/books_list.html', {
        'books': selected_books,
        'previous_date': previous_book and previous_book.pub_date,
        'next_date': next_book and next_book.pub_date
    })
