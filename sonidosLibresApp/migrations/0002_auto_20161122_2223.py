# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-23 03:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sonidosLibresApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]