# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-17 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columnize_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('category', 'name')]),
        ),
    ]