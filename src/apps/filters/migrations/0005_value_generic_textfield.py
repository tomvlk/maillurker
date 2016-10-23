# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0004_add_rule_negat_col'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='value',
            field=models.TextField(),
        ),
    ]
