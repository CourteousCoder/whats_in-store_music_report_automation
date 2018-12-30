# Generated by Django 2.1.4 on 2018-12-30 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('mri_media_id', models.CharField(max_length=32)),
                ('artists', models.ManyToManyField(to='reports.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Spin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_played', models.DateField()),
                ('spin_count', models.IntegerField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.Song')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=127)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=127)),
                ('mri_player_id', models.IntegerField()),
            ],
        ),
    ]