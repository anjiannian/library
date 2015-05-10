# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0001_initial'),
        ('books', '0002_auto_20150430_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='possession',
            name='book',
            field=models.ForeignKey(to='books.Book'),
        ),
        migrations.AddField(
            model_name='possession',
            name='bookshelf',
            field=models.ForeignKey(to='bookshelves.BookShelf'),
        ),
    ]
