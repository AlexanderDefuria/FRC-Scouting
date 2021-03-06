# Generated by Django 2.2 on 2020-04-30 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0008_team_colour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='climb_attempts',
        ),
        migrations.RemoveField(
            model_name='match',
            name='climb_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='defense_time',
        ),
        migrations.RemoveField(
            model_name='match',
            name='game_comments',
        ),
        migrations.RemoveField(
            model_name='match',
            name='initial_comments',
        ),
        migrations.AddField(
            model_name='match',
            name='able_to_push',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='auto_comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='match',
            name='auto_route',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='ball_intake_type',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='dt_fouls',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='field_timeout_pos',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='hp_fouls',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='missed_balls',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='scouter_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='match',
            name='team_defended',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='under_defense',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='match',
            name='yellow_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='climb_location',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense_fouls',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='on_field',
            field=models.BooleanField(default=False),
        ),
    ]
