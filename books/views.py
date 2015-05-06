# -*- coding: utf-8 -*-

from django.http import JsonResponse, HttpResponseBadRequest,
    HttpResponseNotAllowed

from books.forms import FetchBook, UploadBook


def fetch(request):
    """@todo: Docstring for fetch.

    :request: @todo
    :returns: @todo

    """
    if request.method == 'POST':
        form = FetchBook(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data.get('isbn')
            school_id = form.cleaned_data.get('school_id')
            book_shelf = form.cleaned_data.get('book_shelf')
            try:
                if len(isbn) == 10:
                    book = Book.objects.get(isbn10=isbn)
                elif len(isbn) == 13:
                    book = Book.objects.get(isbn13=isbn)
                else:
                    return HttpResponseBadRequest
                if book:
                    BookShelf
            except Exception, e:
                raise e
        else:
            return HttpResponseBadRequest
    else:
        return HttpResponseNotAllowed


def upload(request):
    """@todo: Docstring for upload.

    :request: @todo
    :returns: @todo

    """
    pass
