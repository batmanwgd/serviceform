# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0006_auto_20160508_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceform',
            name='allowed_users',
            field=models.ManyToManyField(blank=True, help_text='Users that are allowed to perform form administration and view reports', related_name='allowed_serviceforms', to=settings.AUTH_USER_MODEL, verbose_name='Allowed users'),
        ),
    ]