# Generated by Django 5.0.4 on 2024-09-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_product_discountedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hero_title', models.CharField(max_length=100)),
                ('energy', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='DiscountedProduct',
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]
