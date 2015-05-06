# -*- coding: utf-8 -*-

from django.db import models

from school.models import School


class BookShelf(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School)
    extra = models.TextField(null=True)
