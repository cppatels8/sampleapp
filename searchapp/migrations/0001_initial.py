# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MPattendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('division_or_seat_num', models.IntegerField(default=0)),
                ('member_name', models.CharField(max_length=200)),
                ('lok_sabha', models.IntegerField(default=0)),
                ('session', models.IntegerField(default=0)),
                ('state', models.CharField(default=None, max_length=200)),
                ('constituency', models.CharField(default=None, max_length=200)),
                ('total_seats', models.IntegerField(default=0)),
                ('num_of_days', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
