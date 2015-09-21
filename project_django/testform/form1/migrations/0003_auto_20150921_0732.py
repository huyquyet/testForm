# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0002_auto_20150921_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
