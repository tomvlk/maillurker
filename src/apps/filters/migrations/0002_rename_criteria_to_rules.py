# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(max_length=255, choices=[('peer', 'Peer Address'), ('port', 'Peer Port'), ('sender_name', 'Sender Name'), ('sender_address', 'Sender Address'), ('recipients_to', 'To Recipients'), ('recipients_cc', 'CC Recipients'), ('recipients_bcc', 'BCC Recipients'), ('subject', 'Subject'), ('size', 'Message Size'), ('type', 'Message Content Type'), ('headers', 'Message Headers')])),
                ('operator', models.CharField(max_length=255, choices=[('iexact', 'Equal Than (==)'), ('icontains', 'Contains'), ('iregex', 'Matches Regular Expression'), ('isnull', 'Is NULL'), ('istrue', 'Is TRUE'), ('isfalse', 'Is FALSE'), ('lt', 'Less Than (<)'), ('gt', 'Greater Than (>)'), ('lte', 'Less or Equal Than (<=)'), ('gte', 'Greater or Equal Than (>=)')])),
                ('value', jsonfield.fields.JSONField()),
                ('filter_set', models.ForeignKey(related_name='rules', to='filters.FilterSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='filter_set',
        ),
        migrations.DeleteModel(
            name='Criteria',
        ),
    ]
