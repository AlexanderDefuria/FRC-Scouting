# Generated by Django 2.2.13 on 2021-01-27 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0034_teammember_tutorial_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_ownership',
            field=models.ForeignKey(default=4490, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team'),
        ),
        migrations.AlterField(
            model_name='pits',
            name='team_ownership',
            field=models.ForeignKey(default=4490, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team'),
        ),
    ]
