# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JoinMe',
        ),
    ]
