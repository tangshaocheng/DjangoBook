# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20150107_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='myactivities',
        ),
    ]
