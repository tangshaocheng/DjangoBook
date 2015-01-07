# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_remove_user_myactivities'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
