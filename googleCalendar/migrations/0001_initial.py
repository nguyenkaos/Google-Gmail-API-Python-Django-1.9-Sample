# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import oauth2client.contrib.django_orm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='googleCalendar.User')),
                ('credential', oauth2client.contrib.django_orm.CredentialsField(null=True)),
            ],
        ),
    ]
