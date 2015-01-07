# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20150107_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='joinme',
            old_name='major',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='joinme',
            name='num',
        ),
        migrations.AddField(
            model_name='activities',
            name='author',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activities',
            name='describe',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joinme',
            name='describe',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='joinme',
            name='email',
            field=models.EmailField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='myactivities',
            field=models.ForeignKey(to='mysite.JoinMe'),
            preserve_default=True,
        ),
    ]
