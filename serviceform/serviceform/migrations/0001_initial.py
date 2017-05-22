# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 10:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import select2.fields
import serviceform.serviceform.models
import serviceform.serviceform.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('multiple_choices_allowed', models.BooleanField(default=True, verbose_name='Multichoice')),
                ('people_needed', models.PositiveIntegerField(default=0, verbose_name='Needed')),
                ('skip_numbering', models.BooleanField(default=False, verbose_name='Skip')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(serviceform.serviceform.models.SubitemMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ActivityChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('people_needed', models.PositiveIntegerField(default=0, verbose_name='Needed')),
                ('skip_numbering', models.BooleanField(default=False, verbose_name='Skip')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Activity')),
            ],
            options={
                'verbose_name': 'Activity choice',
                'verbose_name_plural': 'Activity choices',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(serviceform.serviceform.models.SubitemMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('from_address', models.CharField(max_length=256)),
                ('to_address', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(null=True)),
                ('context', models.TextField(default='{}')),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Template name')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('content', models.TextField(help_text='Following context may (depending on topic) be available for both subject and content: {{responsible}}, {{participant}}, {{last_modified}}, {{form}}, {{url}}, {{contact}}', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Email template',
                'verbose_name_plural': 'Email templates',
            },
            bases=(serviceform.serviceform.models.CopyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FormRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=32, verbose_name='Revision name')),
                ('valid_from', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 22, 20, tzinfo=utc), verbose_name='Valid from')),
                ('valid_to', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 22, 20, tzinfo=utc), verbose_name='Valid to')),
                ('send_bulk_email_to_participants', models.BooleanField(default=True, help_text='Send email to participants that filled the form when this revision was active. Email is sent when new current revision is published.', verbose_name='Send bulk email to participants')),
                ('send_emails_after', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 22, 20, tzinfo=utc), help_text='Sends bulk email to responsibility persons at specified time, after which it will send email for each new participation', verbose_name='Email sending starts')),
            ],
            options={
                'verbose_name': 'Form revision',
                'verbose_name_plural': 'Form revisions',
                'ordering': ('-valid_from',),
            },
        ),
        migrations.CreateModel(
            name='Level1Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('background_color', serviceform.serviceform.models.ColorField(blank=True, null=True, verbose_name='Background color')),
            ],
            options={
                'verbose_name': 'Level 1 category',
                'verbose_name_plural': 'Level 1 categories',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(serviceform.serviceform.models.SubitemMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Level2Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('background_color', serviceform.serviceform.models.ColorField(blank=True, null=True, verbose_name='Background color')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceform.Level1Category', verbose_name='Level 1 category')),
            ],
            options={
                'verbose_name': 'Level 2 category',
                'verbose_name_plural': 'Level 2 categories',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(serviceform.serviceform.models.SubitemMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forenames', models.CharField(max_length=64, verbose_name='Forename(s)')),
                ('surname', models.CharField(max_length=64, verbose_name='Surname')),
                ('street_address', models.CharField(max_length=128, verbose_name='Street address')),
                ('postal_code', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(code='invalid', message='Enter a valid postal code.', regex='^\\d{5}$')], verbose_name='Zip/Postal code')),
                ('city', models.CharField(max_length=32, verbose_name='City')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '050123123' or '+35850123123'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number')),
                ('auth_keys_hash_storage', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('secret_key', models.CharField(db_index=True, default=serviceform.serviceform.utils.generate_uuid, max_length=36, unique=True, verbose_name='Secret key')),
                ('year_of_birth', models.SmallIntegerField(blank=True, null=True, verbose_name='Year of birth')),
                ('status', models.CharField(choices=[('invited', 'invited'), ('ongoing', 'ongoing'), ('updating', 'updating'), ('finished', 'finished')], default='ongoing', max_length=16)),
                ('last_finished_view', models.CharField(default='', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('last_finished', models.DateTimeField(null=True, verbose_name='Last finished')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('send_email_allowed', models.BooleanField(default=True, help_text='You will receive email that contains a link that allows later modification of the form. Also when new version of form is published, you will be notified. It is highly recommended that you keep this enabled unless you move away and do not want to participate at all any more. You can also change this setting later if you wish.', verbose_name='Sending email allowed')),
                ('form_revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceform.FormRevision')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
        ),
        migrations.CreateModel(
            name='ParticipantLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('writer_id', models.PositiveIntegerField()),
                ('message', models.TextField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Participant')),
                ('writer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Activity')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Participant')),
            ],
            options={
                'ordering': ('activity__category__category__order', 'activity__category__order', 'activity__order'),
            },
        ),
        migrations.CreateModel(
            name='ParticipationActivityChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_set', to='serviceform.ParticipationActivity')),
                ('activity_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.ActivityChoice')),
            ],
            options={
                'ordering': ('activity_choice__order',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('question', models.CharField(max_length=1024, verbose_name='Question')),
                ('answer_type', models.CharField(choices=[('integer', 'Integer'), ('short_text', 'Short text'), ('long_text', 'Long text'), ('boolean', 'Boolean'), ('date', 'Date')], default='short_text', max_length=16, verbose_name='Answer type')),
                ('required', models.BooleanField(default=False, verbose_name='Answer required?')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(serviceform.serviceform.models.CopyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Participant')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Question')),
            ],
            options={
                'ordering': ('question__order',),
            },
        ),
        migrations.CreateModel(
            name='ResponsibilityPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forenames', models.CharField(max_length=64, verbose_name='Forename(s)')),
                ('surname', models.CharField(max_length=64, verbose_name='Surname')),
                ('street_address', models.CharField(blank=True, max_length=128, verbose_name='Street address')),
                ('postal_code', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(code='invalid', message='Enter a valid postal code.', regex='^\\d{5}$')], verbose_name='Zip/Postal code')),
                ('city', models.CharField(blank=True, max_length=32, verbose_name='City')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '050123123' or '+35850123123'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number')),
                ('auth_keys_hash_storage', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('secret_key', models.CharField(db_index=True, default=serviceform.serviceform.utils.generate_uuid, max_length=36, unique=True, verbose_name='Secret key')),
                ('send_email_notifications', models.BooleanField(default=True, help_text='Send email notifications whenever new participation to administered activities is registered. Email contains also has a link that allows accessing raport of administered activities.', verbose_name='Send email notifications')),
                ('hide_contact_details', models.BooleanField(default=False, verbose_name='Hide contact details in form')),
                ('show_full_report', models.BooleanField(default=False, verbose_name='Grant access to full reports')),
            ],
            options={
                'verbose_name': 'Responsibility person',
                'verbose_name_plural': 'Responsibility persons',
                'ordering': ('surname',),
            },
            bases=(serviceform.serviceform.models.CopyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServiceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name of the serviceform')),
                ('slug', models.SlugField(help_text='Tämä on osa lomakkeen osoitetta, ts. lomakkeen osoitteeksi tulee http://localhost:8000/valitsemasi-nimi-urlissa', unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last updated')),
                ('require_email_verification', models.BooleanField(default=True, verbose_name='Require email verification')),
                ('password', models.CharField(blank=True, default='', help_text='Password that is asked from participants', max_length=32, verbose_name='Password')),
                ('hide_contact_details', models.BooleanField(default=False, verbose_name='Hide contact details (other than email) in form')),
                ('flow_by_categories', models.BooleanField(default=False, help_text='Please note that preview shows full form despite this option', verbose_name='Split participation form to level 1 categories')),
                ('allow_skipping_categories', models.BooleanField(default=False, help_text='In effect only if flow by categories option is enabled. If this option is enabled, user can jump between categories. If disabled, he must proceed them one by one.', verbose_name='Allow jumping between categories')),
                ('level1_color', serviceform.serviceform.models.ColorField(blank=True, help_text='If left blank (black), default coloring will be used', null=True, verbose_name='Level 1 category default background color')),
                ('level2_color', serviceform.serviceform.models.ColorField(blank=True, help_text='If left blank (black), it will be derived from level 1 background color', null=True, verbose_name='Level 2 category default background color')),
                ('activity_color', serviceform.serviceform.models.ColorField(blank=True, help_text='If left blank (black), it will be derived from level 2 background color', null=True, verbose_name='Activity default background color')),
                ('description', models.TextField(blank=True, help_text='Description box will be shown before instruction box in participation view.', verbose_name='Description')),
                ('instructions', models.TextField(blank=True, help_text='Use HTML formatting. Leave this empty to use default. This is shown in participation view.', null=True, verbose_name='Instructions')),
                ('login_text', models.TextField(blank=True, help_text='This will be shown in the login screen', null=True, verbose_name='Login text')),
                ('required_year_of_birth', models.BooleanField(default=False, verbose_name='Year of birth')),
                ('required_street_address', models.BooleanField(default=True, verbose_name='Street address')),
                ('required_phone_number', models.BooleanField(default=True, verbose_name='Phone number')),
                ('visible_year_of_birth', models.BooleanField(default=True, verbose_name='Year of birth')),
                ('visible_street_address', models.BooleanField(default=True, verbose_name='Street address')),
                ('visible_phone_number', models.BooleanField(default=True, verbose_name='Phone number')),
                ('bulk_email_to_responsibles', models.ForeignKey(blank=True, help_text='Email that is sent to responsibles when emailing starts', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Bulk email to responsibles')),
                ('current_revision', models.ForeignKey(blank=True, help_text='You need to first add a revision to form (see below) and save. Then newly created revision will appear in the list.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceform.FormRevision', verbose_name='Current revision')),
                ('email_to_former_participants', models.ForeignKey(blank=True, help_text='Email that is sent to former participants when form is published', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Bulk email to former participants')),
                ('email_to_invited_users', models.ForeignKey(blank=True, help_text='Email that is sent when user is invited to the form manually via invite form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Invite email')),
                ('email_to_participant', models.ForeignKey(blank=True, help_text='Email that is sent to participant after he has fulfilled his participation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Email to participant, on finish')),
                ('email_to_participant_on_update', models.ForeignKey(blank=True, help_text='Email that is sent to participant after he has updated his participation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Email to participant, on update')),
                ('email_to_responsible_auth_link', models.ForeignKey(blank=True, help_text='Email that is sent to responsible when he requests auth link', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Responsible requests auth link')),
                ('email_to_responsibles', models.ForeignKey(blank=True, help_text='Email that is sent to responsibles when new participation is registered', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Email to responsibles')),
                ('last_editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_serviceform', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by')),
                ('resend_email_to_participant', models.ForeignKey(blank=True, help_text='Email that is sent to participant if he requests resending email', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Resend email to participant')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceform.ResponsibilityPerson', verbose_name='Responsible')),
                ('verification_email_to_participant', models.ForeignKey(blank=True, help_text='Email verification message that is sent to participant when filling form, if email verification is enabled', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='serviceform.EmailTemplate', verbose_name='Verification email to participant')),
            ],
            options={
                'verbose_name': 'Service form',
                'verbose_name_plural': 'Service forms',
            },
            bases=(serviceform.serviceform.models.SubitemMixin, models.Model),
        ),
        migrations.AddField(
            model_name='responsibilityperson',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceform.ServiceForm'),
        ),
        migrations.AddField(
            model_name='question',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.ServiceForm'),
        ),
        migrations.AddField(
            model_name='question',
            name='responsibles',
            field=select2.fields.ManyToManyField(blank=True, related_name='question_related', sorted=False, to='serviceform.ResponsibilityPerson', verbose_name='Responsible persons'),
        ),
        migrations.AddField(
            model_name='level2category',
            name='responsibles',
            field=select2.fields.ManyToManyField(blank=True, related_name='level2category_related', sorted=False, to='serviceform.ResponsibilityPerson', verbose_name='Responsible persons'),
        ),
        migrations.AddField(
            model_name='level1category',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.ServiceForm'),
        ),
        migrations.AddField(
            model_name='level1category',
            name='responsibles',
            field=select2.fields.ManyToManyField(blank=True, related_name='level1category_related', sorted=False, to='serviceform.ResponsibilityPerson', verbose_name='Responsible persons'),
        ),
        migrations.AddField(
            model_name='formrevision',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.ServiceForm', verbose_name='Service form'),
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.ServiceForm'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceform.EmailTemplate'),
        ),
        migrations.AddField(
            model_name='activitychoice',
            name='responsibles',
            field=select2.fields.ManyToManyField(blank=True, related_name='activitychoice_related', sorted=False, to='serviceform.ResponsibilityPerson', verbose_name='Responsible persons'),
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceform.Level2Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='responsibles',
            field=select2.fields.ManyToManyField(blank=True, related_name='activity_related', sorted=False, to='serviceform.ResponsibilityPerson', verbose_name='Responsible persons'),
        ),
        migrations.AlterUniqueTogether(
            name='participationactivitychoice',
            unique_together=set([('activity', 'activity_choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='participationactivity',
            unique_together=set([('participant', 'activity')]),
        ),
        migrations.AlterUniqueTogether(
            name='formrevision',
            unique_together=set([('form', 'name')]),
        ),
    ]
