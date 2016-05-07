# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_industry_location'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.ForeignKey(to='common.Contact')),
                ('organization', models.ForeignKey(related_name='org_contacts', to='organizations.Organization')),
            ],
        ),
    ]
