# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriais', '0003_tutorial_visivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='tutorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutoriais.Tutorial'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='artigo',
            unique_together=set([('id', 'tutorial', 'secao')]),
        ),
    ]