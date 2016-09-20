# -*- coding: utf-8 -*-

from django import forms

from library_sparks.models import Reserve


class ReserveForm(forms.ModelForm):

    class Meta:
        model = Reserve
        fields = ('book',)
