# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('peer', models.CharField(max_length=255)),
                ('port', models.IntegerField(default=None, null=True)),
                ('sender_name', models.CharField(max_length=255, default=None, null=True)),
                ('sender_address', models.CharField(max_length=255)),
                ('recipients_to', jsonfield.fields.JSONField(default=None, null=True)),
                ('recipients_cc', jsonfield.fields.JSONField(default=None, null=True)),
                ('recipients_bcc', jsonfield.fields.JSONField(default=None, null=True)),
                ('subject', models.TextField()),
                ('source', models.TextField(default=None, null=True)),
                ('size', models.IntegerField(default=None, null=True)),
                ('type', models.TextField(default=None, null=True)),
                ('headers', jsonfield.fields.JSONField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessagePart',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_attachment', models.BooleanField()),
                ('type', models.TextField(null=True)),
                ('filename', models.CharField(max_length=512, null=True)),
                ('charset', models.CharField(max_length=255, null=True)),
                ('body', models.TextField(null=True)),
                ('size', models.IntegerField(null=True)),
                ('message', models.ForeignKey(to='mails.Message', related_name='parts')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
