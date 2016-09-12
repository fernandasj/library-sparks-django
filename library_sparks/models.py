# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


# ==============================
# Book
# ==============================


class Book(models.Model):
    disponivel = 'disponivel'
    emprestado = 'emprestado'
    reservado = 'reservado'
    consulta = 'consulta local'
    STATUS_CHOICES = (
        (disponivel, 'disponivel'),
        (emprestado, 'emprestado'),
        (reservado, 'reservado'),
        (consulta, 'consulta local'),
    )

    title = models.CharField(
        'Título',
        max_length=150
    )

    ediction = models.CharField(
        'Local de Edição',
        max_length=65
    )

    edictor = models.CharField(
        'Editora',
        max_length=80
    )

    date_ediction = models.DateField(
        'Data de Edição',
        default=timezone.now()
    )

    status = models.CharField(
        'Status',
        choices=STATUS_CHOICES,
        max_length=65,
        default='disponivel'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

# ============================
# Lending
# ============================


class Lending(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='usuario',
        related_name='lendings',
    )

    book = models.ForeignKey(
        Book,
        verbose_name='livro',
        related_name='lendings',
    )

    date_lending = models.DateField(
        'Data do empréstimo',
        default=timezone.now()
    )

    date_devolution = models.DateField(
        'Data de devolução',
        default=timezone.now(),
        blank=True
    )

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'


# =========================
#  Reserve
# =========================


class Reserve(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='usuario',
        related_name='reserves',
    )

    book = models.ForeignKey(
        Book,
        verbose_name='livro',
        related_name='reserves',
    )

    date_reserve = models.DateField(
        'Data da Reserva',
        default=timezone.now(),
    )

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
