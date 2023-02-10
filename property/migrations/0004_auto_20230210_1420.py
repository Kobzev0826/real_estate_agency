# Generated by Django 2.2.24 on 2023-02-10 11:20

from django.db import migrations


def mark_new_buildings_automatically(apps, schema_editor):
    flat_model = apps.get_model('property', 'Flat')
    for flat in flat_model.objects.all():
        if flat.new_building is not None:
            continue
        if flat.construction_year >= 2015:
            flat.new_building = True
            flat.save()
        else:
            flat.new_building = False
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(mark_new_buildings_automatically),
    ]
