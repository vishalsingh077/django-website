# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logos', '0002_logo_logo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='requested_by',
            field=models.CharField(blank='True', max_length=30),
        ),
        migrations.AlterField(
            model_name='logo',
            name='software_used',
            field=models.CharField(blank='True', max_length=100),
        ),
    ]
