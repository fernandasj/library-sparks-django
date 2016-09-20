# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from library_sparks.models import Book, Reserve
from library_sparks.forms import ReserveForm


@login_required
def index(request):
    return render(request, 'library_sparks/index.html')


def catalogo(request):
    books = Book.objects.all()
    return render(request, 'library_sparks/catalogo.html', {'books': books})


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'library_sparks/detail.html', {'book': book})


def historico(request):
    user = request.user
    return render(request, 'library_sparks/historico.html', {'user': user})


def reserva(request):
    form = ReserveForm()
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            book = reserva.book
            book.status = Book.RESERVADO
            book.save()
            reserva.save()
            return redirect('historico')

        else:
            print form.errors

    return render(request, 'library_sparks/reserva.html', {'form': form})


def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserve, pk=pk)
    book = reserva.book
    book.status = Book.DISPONIVEL
    book.save()
    reserva.delete()
    return redirect('historico')
