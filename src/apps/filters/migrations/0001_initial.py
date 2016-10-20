# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(max_length=255, choices=[('peer', 'Peer Address'), ('port', 'Peer Port'), ('sender_name', 'Sender Name'), ('sender_address', 'Sender Address'), ('recipients_to', 'To Recipients'), ('recipients_cc', 'CC Recipients'), ('recipients_bcc', 'BCC Recipients'), ('subject', 'Subject'), ('size', 'Message Size'), ('type', 'Message Content Type'), ('headers', 'Message Headers')])),
                ('operator', models.CharField(max_length=255, choices=[('iexact', 'Equal Than (==)'), ('icontains', 'Contains'), ('iregex', 'Matches Regular Expression'), ('isnull', 'Is NULL'), ('istrue', 'Is TRUE'), ('isfalse', 'Is FALSE'), ('lt', 'Less Than (<)'), ('gt', 'Greater Than (>)'), ('lte', 'Less or Equal Than (<=)'), ('gte', 'Greater or Equal Than (>=)')])),
                ('value', jsonfield.fields.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('is_global', models.BooleanField(default=False)),
                ('is_active', models.BooleanField()),
                ('icon', models.CharField(default='fa fa-filter', max_length=255, choices=[('fa fa-filter', 'Default Filter'), ('fa fa-server', 'Server')])),
                ('created_by', models.ForeignKey(related_name='created_filters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='criteria',
            name='filter_set',
            field=models.ForeignKey(related_name='criteria', to='filters.FilterSet'),
        ),
    ]
