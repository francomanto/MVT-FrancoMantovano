# Generated by Django 4.1.2 on 2022-10-19 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='dni',
            new_name='edad',
        ),
    ]
