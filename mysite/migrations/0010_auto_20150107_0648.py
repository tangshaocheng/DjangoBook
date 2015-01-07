# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_user_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='myactivities',
            field=models.ManyToManyField(to='mysite.JoinMe'),
            preserve_default=True,
        ),
    ]
