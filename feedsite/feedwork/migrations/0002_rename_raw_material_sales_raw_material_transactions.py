# Generated by Django 3.2.7 on 2022-08-17 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedwork', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='raw_material_sales',
            new_name='raw_material_transactions',
        ),
    ]
