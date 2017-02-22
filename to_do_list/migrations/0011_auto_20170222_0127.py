# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-22 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0010_auto_20170217_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='currenttaskid',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='currenttask',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='to_do_list.Task'),
        ),
    ]
