# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-27 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('publish', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_posts', to='accounts.User')),
                ('likes', models.ManyToManyField(related_name='likes', to='accounts.User')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
    ]
