# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalogo/$', views.catalogo, name='catalogo'),
    url(r'^home/$', views.home, name='home'),
    url(r'^reserva$', views.reserva, name='reserva'),
    url(r'^livro/detail/(?P<pk>[0-9]+)/$', views.detail, name='book_detail'),
    url(r'^reserva/cancelar/(?P<pk>[0-9]+)/$', views.cancelar_reserva, name='reserva_cancelar')
]
