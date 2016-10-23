# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0003_add_combine_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='negate',
            field=models.BooleanField(default=False),
        ),
    ]
