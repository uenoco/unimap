# Generated by Django 3.1.7 on 2021-03-10 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unimap', '0010_auto_20210310_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toilet',
            old_name='Emargencycall',
            new_name='Emergencycall',
        ),
    ]
