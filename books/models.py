# -*- coding: utf-8 -*-

from django.db import models


class Book(models.Model):
    '''
    '''
    app = models.CharField(max_length=100, db_column='app_id', null=True)
    app_key = models.CharField(max_length=100, null=True)
    app_name = models.CharField(max_length=100, null=True)
    callback = models.CharField(max_length=100, null=True)
    company = models.ForeignKey('companies.Company',
                                db_column='company_id', null=True)
    create_time = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    filtercountry = models.CharField(max_length=100,
                                     db_column='filterCountry', null=True)
    online_end_time = models.DateTimeField(null=True)
    online_start_time = models.DateTimeField(null=True)
    revenue_split = models.DecimalField(max_digits=4,
                                        decimal_places=2, null=True)
    sandbox = models.IntegerField(null=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.app_name

    class Meta:
        db_table = 'app'
