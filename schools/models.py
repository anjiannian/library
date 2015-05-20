# -*- coding: utf-8 -*-

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=50, null=True)
    contact_phone = models.CharField(max_length=30, null=True)
    extra = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'school'
