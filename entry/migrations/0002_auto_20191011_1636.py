# Generated by Django 2.2 on 2019-10-11 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='cargo_hatch',
            new_name='ship_hatch',
        ),
    ]
