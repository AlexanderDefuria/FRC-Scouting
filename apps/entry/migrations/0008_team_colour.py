# Generated by Django 2.2 on 2020-04-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0007_auto_20200410_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='colour',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
