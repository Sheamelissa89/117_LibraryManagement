from django.shortcuts import render
from .models import Book


def inventory_view(request):
    books = Book.objects.all().order_by('title')

    context = {
        'books': books,
    }

    return render(request, 'inventory.html', context)