# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in_patient',
            name='date_of_adm',
            field=models.DateField(default=datetime.date(2017, 4, 13)),
        ),
        migrations.AlterField(
            model_name='out_patient',
            name='date',
            field=models.DateField(default=datetime.date(2017, 4, 13)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(default=datetime.date(2017, 4, 13)),
        ),
    ]