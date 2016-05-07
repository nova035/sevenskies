# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160107_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='employee_number',
        ),
    ]
