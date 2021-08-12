# Generated by Django 3.2.6 on 2021-08-12 03:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0019_alter_booklet_subname'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklet',
            name='FileSize',
            field=models.CharField(blank=True, max_length=24, null=True, verbose_name='PDFサイズ'),
        ),
        migrations.AlterField(
            model_name='booklet',
            name='PDFfile',
            field=models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='冊子PDF'),
        ),
    ]