# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150, null=True)),
                ('origin_title', models.CharField(max_length=150, null=True)),
                ('author', models.CharField(max_length=150)),
                ('translator', models.CharField(max_length=150, null=True)),
                ('publisher', models.CharField(max_length=150)),
                ('pubdate', models.DateTimeField()),
                ('binding', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=20)),
                ('pages', models.IntegerField()),
                ('summary', models.TextField(null=True)),
                ('series', models.CharField(max_length=200, null=True)),
                ('isbn10', models.DecimalField(unique=True, max_digits=10, decimal_places=0)),
                ('isbn13', models.DecimalField(unique=True, max_digits=13, decimal_places=0)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
