# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from library_sparks.models import Book, Reserve


@login_required
def index(request):
    return redirect('home')


@login_required
def home(request):
    lendings = request.user.lendings.all
    reserves = request.user.reserves.all

    return render(request, 'library_sparks/home.html', {
        'lendings': lendings,
        'reserves': reserves,
    })


@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'library_sparks/books.html', {
        'books': books
    })


@login_required
def lending_books(request):
    books = Book.objects.filter(status=Book.EMPRESTADO)

    return render(request, 'library_sparks/reserve.html', {
        'books': books
    })


@login_required
def reserve_create(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reserve = Reserve(book=book, user=request.user)
    reserve.save()

    return redirect('home')


@login_required
def reserve_cancel(request, pk):
    reserva = get_object_or_404(Reserve, pk=pk)
    reserva.delete()
    return redirect('home')
