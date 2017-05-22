# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0034_auto_20160513_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='activitychoice',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='level1category',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='level2category',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='responsibilityperson',
            name='send_email_notifications',
            field=models.BooleanField(default=True, help_text='Send email notifications whenever new participation to administered activities is registered. Email contains also has a link that allows accessing raport of administered activities.', verbose_name='Send email notifications'),
        ),
        migrations.AlterField(
            model_name='serviceform',
            name='current_revision',
            field=models.ForeignKey(blank=True, help_text='You need to first add a revision to form (see below) and save. Then newly created revision will appear in the list.', null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceform.FormRevision', verbose_name='Current revision'),
        ),
        migrations.AlterField(
            model_name='serviceform',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]