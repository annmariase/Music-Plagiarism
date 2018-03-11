# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-15 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import signup.models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midiFile', models.FileField(upload_to=signup.models.user_directory_path)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup')),
            ],
        ),
    ]
