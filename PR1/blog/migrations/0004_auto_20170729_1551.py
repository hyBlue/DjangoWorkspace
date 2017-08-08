# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:51
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170729_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(default=(0, 0), help_text=' 경도, 위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
