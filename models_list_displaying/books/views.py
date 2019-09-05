from django.shortcuts import render
from _datetime import date
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_view_by_date(request, year, month, day):
    template = 'books/pub_date_list.html'
    date_filter = date(year, month, day)
    books = Book.objects.filter(pub_date=date_filter)
    try:
        prev_books_date = Book.objects.filter(pub_date__lt=date_filter).values_list('pub_date', flat=True).reverse()[0]
    except IndexError:
        prev_books_date = Book.objects.filter(pub_date=date_filter).values_list('pub_date', flat=True).reverse()[0]
    try:
        next_books_date = Book.objects.filter(pub_date__gt=date_filter).values_list('pub_date', flat=True)[0]
    except IndexError:
        next_books_date = Book.objects.filter(pub_date=date_filter).values_list('pub_date', flat=True)[0]

    context = {
        'books': books,
        'next_url': next_books_date,
        'prev_url': prev_books_date
    }

    return render(request, template, context)

