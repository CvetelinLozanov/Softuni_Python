# Generated by Django 5.1.1 on 2024-09-17 12:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
