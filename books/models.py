# -*- coding: utf-8 -*-

from django.db import models


class Book(models.Model):
    '''
    '''
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, null=True)
    origin_title = models.CharField(max_length=150, null=True)
    author = models.CharField(max_length=150)
    translator = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150)
    pubdate = models.DateTimeField(null=True)
    binding = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=20)
    pages = models.IntegerField()
    summary = models.TextField(null=True)
    series = models.CharField(max_length=200, null=True)
    isbn10 = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    isbn13 = models.DecimalField(max_digits=13, decimal_places=0, unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
