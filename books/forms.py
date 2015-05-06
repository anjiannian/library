# -*- coding: utf-8 -*-

from django import forms


class FetchBook(forms.Form):
    isbn = forms.CharField(max_length=13, required=True)
    school_id = forms.CharField(max_length=10, required=True)
    book_shelf = forms.CharField(max_length=10, required=True)


class UploadBook(forms.Form):
    isbn = forms.CharField(max_length=13, required=True)
    school_id = forms.CharField(max_length=10, required=True)
    book_shelf = forms.CharField(max_length=10, required=True)
    book_name = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=50, required=True)
    publisher = forms.CharField(max_length=100, required=True)
    published = forms.CharField(max_length=8, required=False)
    description = forms.TextField(required=False)
    meta = forms.TextField(required=False)
