# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-04-11 14:42
from __future__ import unicode_literals

from django.db import migrations
import versionfield


class Migration(migrations.Migration):

    dependencies = [
        ('omaha', '0033_auto_20171020_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='version',
            field=versionfield.VersionField(help_text='Format: 255.255.65535.65535', null=True),
        ),
    ]