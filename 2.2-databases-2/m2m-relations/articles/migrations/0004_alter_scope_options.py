# Generated by Django 4.2.3 on 2023-07-28 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main', 'tag']},
        ),
    ]