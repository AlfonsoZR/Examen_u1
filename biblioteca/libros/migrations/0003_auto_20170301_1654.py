# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20170228_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=19999),
        ),
    ]