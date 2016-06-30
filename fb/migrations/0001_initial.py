# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('stop', models.DateTimeField(null=True)),
                ('source', models.CharField(max_length=5000, null=True)),
                ('bad_source', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
