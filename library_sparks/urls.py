# -*- coding: utf-8 -*-

from django.conf.urls import url

from library_sparks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalogo/$', views.books, name='books'),
    url(r'^home/$', views.home, name='home'),
    url(r'^reserva/$', views.lending_books, name='reserve'),
    url(r'^reserva/livro/(?P<pk>[0-9]+)/$', views.reserve_create, name='reserve_create'),
    url(r'^reserva/(?P<pk>[0-9]+)/cancelar/$', views.reserve_cancel, name='reserve_cancel')
]
