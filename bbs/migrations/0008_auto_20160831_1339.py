# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0007_auto_20160831_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(blank=True, height_field='150', null=True, upload_to='uploads', verbose_name='头像', width_field='150'),
        ),
    ]
