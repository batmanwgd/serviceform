# -*- coding: utf-8 -*-
# Generated by Django 1.9.7.dev20160521075240 on 2016-06-22 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0054_auto_20160622_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=36)),
                ('task_id', models.CharField(max_length=36)),
            ],
        ),
        migrations.RemoveField(
            model_name='serviceform',
            name='send_email_task_id',
        ),
        migrations.AddField(
            model_name='scheduledtasks',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='serviceform.ServiceForm'),
        ),
        migrations.AlterUniqueTogether(
            name='scheduledtasks',
            unique_together=set([('form', 'task_type')]),
        ),
    ]