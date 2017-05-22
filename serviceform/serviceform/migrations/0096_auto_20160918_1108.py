# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-18 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0095_auto_20160918_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceform',
            name='required_phone_number',
            field=models.BooleanField(default=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='serviceform',
            name='required_street_address',
            field=models.BooleanField(default=True, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='serviceform',
            name='required_year_of_birth',
            field=models.BooleanField(default=False, verbose_name='Year of birth'),
        ),
        migrations.AddField(
            model_name='serviceform',
            name='visible_phone_number',
            field=models.BooleanField(default=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='serviceform',
            name='visible_street_address',
            field=models.BooleanField(default=True, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='serviceform',
            name='visible_year_of_birth',
            field=models.BooleanField(default=True, verbose_name='Year of birth'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='year_of_birth',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Year of birth'),
        ),
    ]