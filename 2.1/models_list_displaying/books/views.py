from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    books = Book.objects.all()
    page_number = request.GET.get('page')
    
    paginator = Paginator(books, 3)
    page = paginator.get_page(page_number)
    
    context['page'] = page

    return render(request, template, context)


def books_by_date(request, pub_date):
    book_list = Book.objects.filter(pub_date=pub_date).order_by('id')
    paginator = Paginator(book_list, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    prev_date = Book.objects.filter(
        pub_date__lt=pub_date
        ).order_by('-pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'page_obj': page_obj,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, 'books/book_pub.html', context)
