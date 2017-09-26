# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillableService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr1', models.TextField()),
                ('attr2', models.TextField()),
                ('fk', models.ManyToManyField(related_name='_node_fk_+', to='app.Node')),
                ('m2m', models.ManyToManyField(related_name='_node_m2m_+', to='app.Node')),
                ('one_to_one', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reverse_one_to_one', to='app.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claim', to='app.Order'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.InsurancePayer'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='services',
            field=models.ManyToManyField(to='app.BillableService'),
        ),
    ]