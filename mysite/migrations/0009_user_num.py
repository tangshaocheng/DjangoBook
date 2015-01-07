# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20150107_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
