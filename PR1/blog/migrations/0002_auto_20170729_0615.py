# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 21:15
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(default=django.utils.timezone.now, help_text=' 경도, 위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
