# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20170821_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_detail_postcode',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_detail_postcode',
            field=models.CharField(default='BT66EY', max_length=10, verbose_name='Zip/Postcode'),
            preserve_default=False,
        ),
    ]