# Generated by Django 2.2 on 2019-10-01 21:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='NA')),
                ('TBA_key', models.TextField(default='NA')),
                ('TBA_eventType', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('start', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000000), django.core.validators.MinValueValidator(0)])),
                ('imported', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(default='team', max_length=100)),
                ('TBA_key', models.TextField(default='NA', max_length=40)),
                ('event_five', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Event')),
                ('event_four', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Event')),
                ('event_one', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Event')),
                ('event_three', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Event')),
                ('event_two', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('TBA_key', models.TextField(default='NA', max_length=40)),
                ('red_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)])),
                ('blue_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)])),
                ('played', models.BooleanField(default=False)),
                ('blue1', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
                ('blue2', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
                ('blue3', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
                ('event', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Event')),
                ('red1', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
                ('red2', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
                ('red3', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='entry.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)])),
                ('auto_cargo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('first_cargo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('second_cargo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('third_cargo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('ship_cargo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(0)])),
                ('auto_hatch', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('first_hatch', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('second_hatch', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('third_hatch', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('cargo_hatch', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(0)])),
                ('climb', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)])),
                ('first_start', models.BooleanField(default=True)),
                ('second_start', models.BooleanField(default=False)),
                ('defense_time', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(135000), django.core.validators.MinValueValidator(1)])),
                ('event', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Event')),
                ('team', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entry.Team')),
            ],
        ),
    ]
