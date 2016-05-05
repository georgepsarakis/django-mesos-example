# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.TextField()),
                ('context', models.TextField()),
                ('engine', models.CharField(choices=[('django', 'django'), ('jinja', 'jinja')], max_length=50)),
                ('processed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
