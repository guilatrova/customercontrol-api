# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=25)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]