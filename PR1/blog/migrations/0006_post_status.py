# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170729_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
