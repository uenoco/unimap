# Generated by Django 3.2.6 on 2021-08-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0020_auto_20210812_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='DisplayFlag',
            field=models.BooleanField(default=False, verbose_name='表示ON/OFF'),
        ),
    ]
