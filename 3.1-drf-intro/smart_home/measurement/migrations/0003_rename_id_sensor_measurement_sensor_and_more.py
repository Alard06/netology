# Generated by Django 4.2.4 on 2023-08-11 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_date_measurement_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor',
        ),
        migrations.RenameField(
            model_name='measurement',
            old_name='t',
            new_name='temperature',
        ),
    ]