# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0002_rename_criteria_to_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterset',
            name='combine',
            field=models.CharField(default='and', max_length=3, choices=[('and', 'Match all criteria (AND)'), ('or', 'Match one of the criteria (OR)')]),
        ),
    ]
