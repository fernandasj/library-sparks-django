# -*- coding: utf-8 -*-

from django.contrib import admin

from library_sparks.models import Book, Lending, Reserve


# ==============================
# BookAdmin
# ==============================


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'edictor', 'ediction', 'date_ediction', 'status')
    ordering = ('id',)


admin.site.register(Book, BookAdmin)


# ==============================
# LendingAdmin
# ==============================


class LendingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'date_lending', 'date_devolution')
    ordering = ('date_devolution', 'date_lending')


admin.site.register(Lending, LendingAdmin)


# ==============================
# LendingAdmin
# ==============================


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'date_reserve')
    ordering = ('date_reserve',)


admin.site.register(Reserve, ReserveAdmin)
