# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriais', '0004_auto_20161114_1709'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='artigo',
            unique_together=set([('id', 'secao')]),
        ),
    ]
