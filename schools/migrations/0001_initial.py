# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('contact_phone', models.CharField(max_length=30, null=True)),
                ('extra', models.TextField(null=True)),
            ],
        ),
    ]
