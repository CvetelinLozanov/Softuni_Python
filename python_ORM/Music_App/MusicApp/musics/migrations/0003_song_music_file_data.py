# Generated by Django 5.1.1 on 2024-09-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0002_alter_album_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='music_file_data',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
