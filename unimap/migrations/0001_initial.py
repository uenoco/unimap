# Generated by Django 3.1.7 on 2021-03-08 07:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Border',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n03_001', models.CharField(max_length=10, verbose_name='都道府県名')),
                ('n03_002', models.CharField(blank=True, max_length=20, verbose_name='支庁名')),
                ('n03_003', models.CharField(blank=True, max_length=20, verbose_name='群・政令市名')),
                ('n03_004', models.CharField(blank=True, max_length=20, verbose_name='市区町村名')),
                ('n03_007', models.CharField(max_length=5, verbose_name='行政区域コード')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'verbose_name': '行政区域',
                'verbose_name_plural': '行政区域一覧',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=128, verbose_name='コース名')),
                ('CourseAbstruct', models.CharField(max_length=256, verbose_name='概要')),
            ],
            options={
                'verbose_name': '推奨ルート',
                'verbose_name_plural': '推奨ルート',
            },
        ),
    ]
