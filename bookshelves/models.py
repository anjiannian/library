# -*- coding: utf-8 -*-

from django.db import models

from schools.models import School


class BookShelf(models.Model):
    name = models.CharField(max_length=20, null=True)
    school = models.ForeignKey(School)
    extra = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'bookshelf'
