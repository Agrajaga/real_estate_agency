# Generated by Django 2.2.24 on 2022-03-28 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220328_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='user',
            new_name='complainant',
        ),
    ]
