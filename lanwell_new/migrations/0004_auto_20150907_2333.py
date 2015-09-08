# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanwell_new', '0003_customerrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='description',
            field=models.CharField(max_length=2000, blank=True, verbose_name='Суть проблемы*'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='email',
            field=models.EmailField(max_length=254, blank=True, verbose_name='e-mail*'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Ваше имя*'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='phone',
            field=models.CharField(max_length=50, blank=True, verbose_name='Ваш телефон'),
        ),
    ]
