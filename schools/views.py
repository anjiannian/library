# -*- coding: utf-8 -*-

from django.http import JsonResponse

from schools.models import School
from bookshelves.models import BookShelf


def list(request):
    """
    This function is used to list all schools
    and the bookshelves pocessed
    TODO: bookshelf.name
    """

    schools = School.objects.all()
    bookshelves = BookShelf.objects.all()
    res = []
    if schools:
        state = 0
        for school in schools:
            res.append({
                'school_id': school.id,
                'school_name': school.name,
                'bookshelf': [bookshelf.name for bookshelf in bookshelves
                              if bookshelf.school == school]
            })
    else:
        state = 1
    return JsonResponse({'state': state, 'schools': res})
