# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-17 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columnize_menu', '0002_auto_20160617_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=254),
        ),
    ]
