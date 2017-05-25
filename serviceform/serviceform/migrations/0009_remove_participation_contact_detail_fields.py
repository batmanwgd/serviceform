# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceform', '0008_add_member_and_organization_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='forenames',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='year_of_birth',
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name': 'Participation', 'verbose_name_plural': 'Participations'},
        ),
        migrations.RemoveField(
            model_name='participation',
            name='auth_keys_hash_storage',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='secret_key',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='send_email_allowed',
        ),
    ]
