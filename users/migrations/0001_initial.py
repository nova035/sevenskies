# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 20:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=60)),
                ('other_names', models.CharField(blank=True, default='', max_length=80)),
                ('username', models.CharField(blank=True, max_length=60, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Preferred name contain only letters numbers or underscores', regex='^\\w+$')])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('search', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee_number', models.CharField(max_length=20, unique=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.CustomUser')),
            ],
            options={
                'ordering': ('-date_joined',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='A short name for the job title', max_length=100, unique=True)),
                ('abbreviation', models.CharField(blank=True, help_text='The short name for the title', max_length=100, null=True)),
                ('description', models.TextField(blank=True, help_text='A short summary of the job title', null=True)),
                ('search', models.TextField(blank=True, help_text='A dummy field to enable search on the model through a filter', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-created',),
                'permissions': (('view_jobtitle', 'Can view job title'),),
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='job_title',
            field=models.ForeignKey(blank=True, help_text='The job title of the user', null=True, on_delete=django.db.models.deletion.PROTECT, to='users.JobTitle'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.CustomUser'),
        ),
    ]