# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customoauthapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customoauthapplication',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomOAuthApplication',
        ),
    ]
