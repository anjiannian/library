# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20150509_1719'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='possession',
            table='possession',
        ),
    ]
