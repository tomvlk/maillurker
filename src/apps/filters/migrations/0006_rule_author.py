# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filters', '0005_value_generic_textfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='created_by',
            field=models.ForeignKey(default=None, related_name='created_rules', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
