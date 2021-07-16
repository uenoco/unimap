# Generated by Django 3.2.3 on 2021-07-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0007_alter_pointdata_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointdata',
            name='Sort',
            field=models.IntegerField(choices=[(1, 'route'), (2, 'start'), (3, 'end'), (4, 'start_op'), (5, 'end_op'), (6, 'location'), (7, 'barrguide'), (8, 'attension'), (9, 'caution'), (10, 'busstop'), (11, 'shop')], default=1, verbose_name='地点タイプ'),
        ),
    ]