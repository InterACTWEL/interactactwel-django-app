# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-02 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactwel', '0009_interactwelplan_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactwelplan',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='plans', to='interactwel.InteractwelActor'),
        ),
    ]
