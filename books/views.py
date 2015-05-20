# -*- coding: utf-8 -*-

import json
import urllib2
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, \
    HttpResponseNotAllowed

from bookshelves.models import BookShelf
from books.models import Book, Possession
from books.forms import FetchBook, UploadBook
from library.utils import to_isbn10, to_isbn13

URL = "https://api.douban.com/v2/book/isbn/"


@csrf_exempt
def fetch(request):
    """
    """

    if request.method == 'POST':
        form = FetchBook(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data.get('isbn')
            book_shelf = form.cleaned_data.get('book_shelf')
            try:
                # Check database first
                if len(isbn) == 10:
                    book = Book.objects.filter(isbn10=isbn).first()
                elif len(isbn) == 13:
                    book = Book.objects.filter(isbn13=isbn).first()
                else:
                    return HttpResponseBadRequest("isbn not right")

                # if nothing found get from douban
                if not book:
                    book = get_book(isbn)
                # still nothing, return
                if book:
                    bookshelf = BookShelf.objects.get(id=book_shelf)
                    possession = Possession.objects.filter(
                        book=book, bookshelf=bookshelf).first()
                    if possession:
                        possession.count += 1
                        possession.save()
                        return JsonResponse({'result': 1})
                    else:
                        possession = Possession.objects.create(
                            book=book, bookshelf=bookshelf)
                        return JsonResponse({'result': 0})
                else:
                    return JsonResponse({'result': 2})
            except:
                return HttpResponseBadRequest("Check your params")
        else:
            return HttpResponseBadRequest("Check your params")
    else:
        return HttpResponseNotAllowed("Only POST method is allowed here.")


@csrf_exempt
def upload(request):
    """
    """
    if request.method == 'POST':
        form = UploadBook(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data.get('isbn')
            book_shelf = form.cleaned_data.get('book_shelf')
            book_name = form.cleaned_data.get('book_name')
            author = form.cleaned_data.get('author')
            publisher = form.cleaned_data.get('publisher')
            published = form.cleaned_data.get('published')
            description = form.cleaned_data.get('description')
            meta = form.cleaned_data.get('meta')
            if len(isbn) == 10:
                isbn10 = isbn
                isbn13 = to_isbn13(isbn)
            elif len(isbn) == 13:
                isbn13 = isbn
                isbn10 = to_isbn10(isbn)
            else:
                return HttpResponseBadRequest("isbn is not right")
            authors = []
            authors.append(author)
            try:
                book = Book.objects.create(
                    title=book_name, author=json.dumps(authors),
                    publisher=publisher, pubdate=published, isbn10=isbn10,
                    isbn13=isbn13, summary=meta+description)
                bookshelf = BookShelf.objects.get(id=book_shelf)
                Possession.objects.create(bookshelf=bookshelf, book=book)
                return JsonResponse({'result': 0})
            except:
                return HttpResponseBadRequest("Check your params")
        else:
            return HttpResponseBadRequest("Check your params")
    else:
        return HttpResponseNotAllowed("Only POST method is allowed here.")


def get_book(isbn):
    """
    Get the book from douban api directly
    if not found in database
    """
    try:
        resp = urllib2.urlopen(URL+isbn)
        data = json.loads(resp.read())
        series = data.get('series', '')
        if series:
            series['title'] = series['title'].encode('utf-8')
        book = Book.objects.create(
            title=data['title'].encode('utf-8'),
            subtitle=data['subtitle'].encode('utf-8'),
            origin_title=data['origin_title'].encode('utf-8'),
            author=json.dumps(data['author']),
            translator=json.dumps(data['translator']),
            publisher=data['publisher'].encode('utf-8'),
            pubdate=data['pubdate'],
            binding=data['binding'].encode('utf-8'),
            price=data['price'],
            pages=data['pages'],
            summary=data['summary'].encode('utf-8'),
            series=json.dumps(series),
            isbn10=data['isbn10'],
            isbn13=data['isbn13'],
            created=datetime.now())
        return book
    except:
        return None
