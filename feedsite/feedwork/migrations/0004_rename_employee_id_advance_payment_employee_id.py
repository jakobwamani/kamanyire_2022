# Generated by Django 3.2.7 on 2022-08-13 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedwork', '0003_auto_20220813_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advance_payment',
            old_name='Employee_id',
            new_name='employee_id',
        ),
    ]
