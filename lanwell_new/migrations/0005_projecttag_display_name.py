# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanwell_new', '0004_auto_20150907_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttag',
            name='display_name',
            field=models.CharField(default='Категория', max_length=200),
            preserve_default=False,
        ),
    ]
