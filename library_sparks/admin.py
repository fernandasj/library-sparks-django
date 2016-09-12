from django.contrib import admin

from .models import Book, Lending, Reserve

# ====================
# BookAdmin
# ====================


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Book, BookAdmin)

# ====================
# LendingAdmin
# ====================


class LendingAdmin(admin.ModelAdmin):
    list_display = ('book',)

admin.site.register(Lending, LendingAdmin)

# ====================
# LendingAdmin
# ====================


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('book',)

admin.site.register(Reserve, ReserveAdmin)

