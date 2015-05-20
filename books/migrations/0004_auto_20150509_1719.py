# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150509_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn10',
            field=models.CharField(unique=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^.{10}$', message=b'Length has to be 10', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(unique=True, max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^.{13}$', message=b'Length has to be 13', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
