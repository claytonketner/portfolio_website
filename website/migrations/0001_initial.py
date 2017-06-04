# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-04 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300, unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
