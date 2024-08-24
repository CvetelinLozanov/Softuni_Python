# Generated by Django 5.0.4 on 2024-08-23 11:53

from django.db import migrations


class Migration(migrations.Migration):

    def create_unique_brands(apps, schema_editor):
        shoe = apps.get_model('main_app', 'Shoe')
        unique_brands = apps.get_model('main_app', 'UniqueBrands')

        db_alias = schema_editor.connection.alias

        unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

        for brand_name in unique_brand_names:
            unique_brands.objects.using(db_alias).create(brand_name=brand_name)

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands)
    ]
