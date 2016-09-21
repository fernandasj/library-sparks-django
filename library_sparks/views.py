# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from library_sparks.models import Book, Reserve
from library_sparks.forms import ReserveForm


@login_required
def index(request):
    return redirect('home')


def catalogo(request):
    books = Book.objects.all()
    return render(request, 'library_sparks/catalogo.html', {'books': books})


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'library_sparks/detail.html', {'book': book})


@login_required
def home(request):
    lendings = request.user.lendings.all
    reserves = request.user.reserves.all
    return render(request, 'library_sparks/home.html', {
        'lendings': lendings,
        'reserves': reserves,
        }
    )


def reserva(request):
    form = ReserveForm()
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            reserva.save()
            return redirect('home')
        else:
            print form.errors

    return render(request, 'library_sparks/reserva.html', {'form': form})


def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserve, pk=pk)
    book = reserva.book
    book.status = Book.DISPONIVEL
    book.save()
    reserva.delete()
    return redirect('home')
