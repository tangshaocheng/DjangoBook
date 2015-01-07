# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_delete_testgood'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='urlButton',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
