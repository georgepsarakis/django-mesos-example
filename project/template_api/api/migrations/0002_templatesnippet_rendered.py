# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatesnippet',
            name='rendered',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
