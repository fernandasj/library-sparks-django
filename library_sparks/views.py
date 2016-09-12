from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from library_sparks.models import Book


@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'library_sparks/index.html', {'books': books})
