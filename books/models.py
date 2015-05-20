# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator

from bookshelves.models import BookShelf


class Book(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, null=True)
    origin_title = models.CharField(max_length=150, null=True)
    author = models.CharField(max_length=150)
    translator = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150)
    pubdate = models.CharField(max_length=30, null=True)
    binding = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=20, null=True)
    pages = models.IntegerField(null=True)
    summary = models.TextField(null=True)
    series = models.CharField(max_length=300, null=True)
    isbn10 = models.CharField(
        max_length=10, unique=True, validators=[RegexValidator(
            regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    isbn13 = models.CharField(
        max_length=13, unique=True, validators=[RegexValidator(
            regex='^.{13}$', message='Length has to be 13', code='nomatch')])
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'book'


class Possession(models.Model):
    bookshelf = models.ForeignKey(BookShelf)
    book = models.ForeignKey(Book)
    count = models.IntegerField(default=1)

    def __unicode__(self):
        return self.book.title

    class Meta:
        db_table = 'possession'
