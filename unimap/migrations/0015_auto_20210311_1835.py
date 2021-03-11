# Generated by Django 3.1.7 on 2021-03-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0014_auto_20210311_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='Zoom',
            new_name='DEF_Zoom',
        ),
        migrations.RemoveField(
            model_name='imagemap',
            name='Name',
        ),
        migrations.AddField(
            model_name='imagemap',
            name='ImageMap',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='イラスト地図'),
        ),
    ]
