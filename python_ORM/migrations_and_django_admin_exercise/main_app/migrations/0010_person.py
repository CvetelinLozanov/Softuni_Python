# Generated by Django 5.0.4 on 2024-08-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=40)),
                ('age', models.PositiveIntegerField()),
                ('age_group', models.CharField(default='No age group', max_length=20)),
            ],
        ),
    ]
