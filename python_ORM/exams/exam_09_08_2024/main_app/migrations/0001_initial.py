# Generated by Django 5.0.4 on 2024-09-22 17:50

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('motto', models.TextField(blank=True, null=True)),
                ('is_ruling', models.BooleanField(default=False)),
                ('castle', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('power', models.DecimalField(decimal_places=1, default=1, max_digits=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('breath', models.CharField(choices=[('Fire', 'Fire'), ('Ice', 'Ice'), ('Lightning', 'Lightning'), ('Unknown', 'Unknown')], default='Unknown', max_length=9)),
                ('is_healthy', models.BooleanField(default=True)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dragons', to='main_app.house')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z#]{4}$')])),
                ('reward', models.FloatField(default=100)),
                ('start_time', models.DateTimeField()),
                ('dragons', models.ManyToManyField(related_name='quests', to='main_app.dragon')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='main_app.house')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
