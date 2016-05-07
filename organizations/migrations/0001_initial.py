# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_industry_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=b'-')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('industry', models.ForeignKey(to='common.Industry')),
                ('location', models.ForeignKey(to='common.Location')),
            ],
        ),
    ]
