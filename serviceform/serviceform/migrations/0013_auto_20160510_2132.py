# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0012_auto_20160510_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='order_hint',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, help_text='Items are ordered by this field. This field is automatically filled if not given.', max_digits=5, max_length=5, null=True, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='activitychoice',
            name='order_hint',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, help_text='Items are ordered by this field. This field is automatically filled if not given.', max_digits=5, max_length=5, null=True, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='level1category',
            name='order_hint',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, help_text='Items are ordered by this field. This field is automatically filled if not given.', max_digits=5, max_length=5, null=True, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='level2category',
            name='order_hint',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, help_text='Items are ordered by this field. This field is automatically filled if not given.', max_digits=5, max_length=5, null=True, verbose_name='Order hint'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order_hint',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, help_text='Items are ordered by this field. This field is automatically filled if not given.', max_digits=5, max_length=5, null=True, verbose_name='Order hint'),
        ),
    ]