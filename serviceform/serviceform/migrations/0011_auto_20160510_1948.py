# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0010_auto_20160510_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='order_hint',
            field=models.DecimalField(blank=True, null=True, db_index=True, decimal_places=2, max_digits=5, max_length=5, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='activitychoice',
            name='order_hint',
            field=models.DecimalField(blank=True, null=True, db_index=True, decimal_places=2, max_digits=5, max_length=5, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='level1category',
            name='order_hint',
            field=models.DecimalField(blank=True, null=True, db_index=True, decimal_places=2, max_digits=5, max_length=5, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='level2category',
            name='order_hint',
            field=models.DecimalField(blank=True, null=True, db_index=True, decimal_places=2, max_digits=5, max_length=5, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order_hint',
            field=models.DecimalField(blank=True, null=True, db_index=True, decimal_places=2, max_digits=5, max_length=5, verbose_name='Order hint'),
        ),
    ]