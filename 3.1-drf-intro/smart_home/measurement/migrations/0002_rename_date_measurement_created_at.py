# Generated by Django 4.2.4 on 2023-08-11 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date',
            new_name='created_at',
        ),
    ]
