# Generated by Django 3.2.3 on 2021-05-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imagemap',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pointdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slope',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='toilet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='zone',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
