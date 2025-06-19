from django.urls import path
from api.v1.books.views import books, update_book, delete_book, add_book, rented, rent_book, rent_out, return_book, mark_overdue_books


urlpatterns = [
    path('',books),
    path('update-book/<int:pk>/', update_book),
    path('delete-book/<int:pk>/', delete_book),
    path('add-book/', add_book),
    path('rented-history/', rented),
    path('rent-book/', rent_book),
    path('rent-out/', rent_out),
    path('return-book/<int:pk>/', return_book),
    path('overdue_books/',mark_overdue_books)
]
