# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='status',
            field=models.IntegerField(choices=[(0, '\u6b63\u5728\u8fd0\u884c'), (1, '\u8fd0\u884c\u6210\u529f'), (2, '\u8fd0\u884c\u5931\u8d25')], default=0),
        ),
    ]
