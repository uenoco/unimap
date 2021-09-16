# Generated by Django 3.2.6 on 2021-09-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0028_auto_20210906_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='ImageAdd1',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='ImageAdd2',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Photo1',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Photo2',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Photo3',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Photo360',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Photo360_2',
        ),
        migrations.AddField(
            model_name='hotel',
            name='ImageBath',
            field=models.ImageField(blank=True, null=True, upload_to='photos/hotel/', verbose_name='浴室画像'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='ImageToilet',
            field=models.ImageField(blank=True, null=True, upload_to='photos/hotel/', verbose_name='トイレ画像'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='Photo360bath',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to='', verbose_name='浴室画像360URL'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='Photo360room',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='部屋画像360URL'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='Photo360toilet',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to='', verbose_name='トイレ画像360URL'),
        ),
    ]
