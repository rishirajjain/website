# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('event_type', models.CharField(choices=[(b'scholarship', b'Scholarship'), (b'workshop', b'Workshop'), (b'internship', b'Internship'), (b'conference', b'Conference'), (b'contest', b'Contest'), (b'techfest', b'Tech-Fest'), (b'others', b'Others')], max_length=15)),
                ('deadline', models.DateField()),
                ('event_url', models.URLField()),
            ],
        ),
    ]
