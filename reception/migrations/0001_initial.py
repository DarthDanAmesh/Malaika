# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('malaika', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='In_patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_adm', models.DateField(default=datetime.date(2017, 4, 12))),
                ('date_of_discarge', models.DateField()),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malaika.Diagnose')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Out_patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2017, 4, 12))),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malaika.Diagnose')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dob', models.DateField(default=datetime.date(2017, 4, 12))),
                ('age', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=200)),
                ('next_of_kin', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='out_patient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.Patient'),
        ),
        migrations.AddField(
            model_name='in_patient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.Patient'),
        ),
        migrations.AddField(
            model_name='in_patient',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malaika.Room'),
        ),
    ]
