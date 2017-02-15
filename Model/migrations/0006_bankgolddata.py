# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0005_fundnetdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankGoldData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=200)),
                ('midpri', models.FloatField()),
                ('buypri', models.FloatField()),
                ('sellpri', models.FloatField()),
                ('maxpri', models.FloatField()),
                ('minpri', models.FloatField()),
                ('todayopen', models.FloatField()),
                ('closeyes', models.FloatField()),
                ('quantpri', models.FloatField()),
                ('time', models.CharField(max_length=200)),
            ],
        ),
    ]