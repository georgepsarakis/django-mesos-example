# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_templatesnippet_rendered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatesnippet',
            name='user',
        ),
        migrations.AddField(
            model_name='templatesnippet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='templatesnippet',
            name='engine',
            field=models.CharField(choices=[('jinja2', 'jinja2'), ('django', 'django')], max_length=50),
        ),
    ]