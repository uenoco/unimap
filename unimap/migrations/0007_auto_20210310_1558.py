# Generated by Django 3.1.7 on 2021-03-10 06:58

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.linestring
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0006_auto_20210310_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sort', models.IntegerField(choices=[(101, 'hotel'), (999, 'etc')], default=101, verbose_name='地点タイプ')),
                ('Name', models.CharField(max_length=32, verbose_name='名称')),
                ('Summery', models.CharField(max_length=256, null=True, verbose_name='概要')),
                ('Telephon', models.CharField(max_length=32, verbose_name='電話')),
                ('Address', models.CharField(max_length=256, verbose_name='住所')),
                ('Url', models.CharField(max_length=256, verbose_name='URL')),
                ('Url_F21', models.CharField(max_length=256, verbose_name='URL_F21')),
                ('Photo1', models.CharField(max_length=256, null=True, verbose_name='Photo1')),
                ('Photo2', models.CharField(max_length=256, null=True, verbose_name='Photo2')),
                ('Photo3', models.CharField(max_length=256, null=True, verbose_name='Photo3')),
                ('Photo360', models.CharField(max_length=256, null=True, verbose_name='Photo360')),
                ('Photo360_2', models.CharField(max_length=256, null=True, verbose_name='Photo360_2')),
                ('geom', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point([135.82, 34.68]), srid=4326)),
            ],
            options={
                'verbose_name': 'A2.ホテル情報',
                'verbose_name_plural': 'A2.ホテル情報',
            },
        ),
        migrations.CreateModel(
            name='Slope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sort', models.IntegerField(choices=[(1, 'ゆるい坂'), (2, '中くらいの坂'), (3, '急な坂')], default=1, verbose_name='坂タイプ')),
                ('Name', models.CharField(max_length=32, verbose_name='名称')),
                ('Summery', models.CharField(max_length=256, null=True, verbose_name='概要')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(default=django.contrib.gis.geos.linestring.LineString([135.82, 34.681], [135.83, 34.68]), srid=4326)),
            ],
            options={
                'verbose_name': '3.ルート補足',
                'verbose_name_plural': '3.ルート補足',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sort', models.IntegerField(choices=[(1, 'gravel'), (2, 'difficulty'), (3, 'impassable'), (4, 'traffic')], default=1, verbose_name='ゾーンタイプ')),
                ('Name', models.CharField(max_length=32, verbose_name='名称')),
                ('Summery', models.CharField(max_length=256, null=True, verbose_name='概要')),
                ('Photo1', models.CharField(max_length=256, null=True, verbose_name='Photo1')),
                ('Photo2', models.CharField(max_length=256, null=True, verbose_name='Photo2')),
                ('Photo3', models.CharField(max_length=256, null=True, verbose_name='Photo3')),
                ('Photo360', models.CharField(max_length=256, null=True, verbose_name='Photo360')),
                ('Photo360_2', models.CharField(max_length=256, null=True, verbose_name='Photo360_2')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'verbose_name': '5.ゾーン情報',
                'verbose_name_plural': '5.ゾーン情報',
            },
        ),
        migrations.DeleteModel(
            name='Border',
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '1.マップエリア', 'verbose_name_plural': '1.マップエリア'},
        ),
        migrations.AlterModelOptions(
            name='pointdata',
            options={'verbose_name': '2.地点情報', 'verbose_name_plural': '2.地点情報'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': '2.推奨ルート', 'verbose_name_plural': '2.推奨ルート'},
        ),
        migrations.AlterModelOptions(
            name='toilet',
            options={'verbose_name': 'A1.トイレ情報', 'verbose_name_plural': 'A1.トイレ情報'},
        ),
        migrations.AlterField(
            model_name='route',
            name='Sort',
            field=models.IntegerField(choices=[(1, 'main'), (2, 'option')], default=100, verbose_name='ルート種類'),
        ),
        migrations.AlterField(
            model_name='route',
            name='geom',
            field=django.contrib.gis.db.models.fields.LineStringField(default=django.contrib.gis.geos.linestring.LineString([135.82, 34.681], [135.83, 34.685]), srid=4326),
        ),
        migrations.AddField(
            model_name='zone',
            name='AreaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unimap.area', verbose_name='エリアID'),
        ),
        migrations.AddField(
            model_name='slope',
            name='AreaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unimap.area', verbose_name='エリアID'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='AreaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unimap.area', verbose_name='エリアID'),
        ),
    ]