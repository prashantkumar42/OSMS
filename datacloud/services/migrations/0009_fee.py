# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-16 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20161216_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField()),
                ('installments', models.IntegerField()),
                ('amountPerInst', models.IntegerField()),
                ('paidInst', models.IntegerField()),
            ],
        ),
    ]