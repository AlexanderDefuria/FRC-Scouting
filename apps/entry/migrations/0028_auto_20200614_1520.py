# Generated by Django 2.2.13 on 2020-06-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0027_auto_20200613_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='position',
            field=models.CharField(choices=[('NA', 'No Access'), ('OV', 'Only View'), ('MS', 'Match Scout'), ('PS', 'Pit Scout'), ('GS', 'General Scout'), ('DT', 'Drive Team'), ('LS', 'Lead Scout')], default='GS', max_length=2),
        ),
    ]
