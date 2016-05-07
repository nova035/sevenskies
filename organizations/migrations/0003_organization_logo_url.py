# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organizationcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
