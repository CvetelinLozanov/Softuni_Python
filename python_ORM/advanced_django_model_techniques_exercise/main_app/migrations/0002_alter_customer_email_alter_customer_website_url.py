# Generated by Django 5.0.4 on 2024-09-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(error_messages={'Invalid': 'Enter a valid email address'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website_url',
            field=models.URLField(error_messages={'Invalid': 'Enter a valid URL'}),
        ),
    ]
