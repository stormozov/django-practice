from django.urls import path

from books.views import books_details, books_list

urlpatterns = [
    path('', books_list, name='books_list'),
    path('<str:pub_date>', books_details, name='books_details'),
]