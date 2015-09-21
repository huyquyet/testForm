# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='birthday',
            field=models.DateTimeField(),
        ),
    ]
