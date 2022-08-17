# Generated by Django 3.2.7 on 2022-08-17 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone_number_one', models.CharField(max_length=50)),
                ('phone_number_two', models.CharField(max_length=50)),
                ('employment_start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='expense_names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('expense_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='expense_units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('unit_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product_names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('product_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='raw_materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('raw_material_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('supplier_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='salary_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('salary', models.IntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.employee')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_separations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('separation_name', models.CharField(max_length=50)),
                ('ratio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.product_names')),
                ('raw_material_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.raw_materials')),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('unit_price', models.IntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('raw_material_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.raw_materials')),
            ],
        ),
        migrations.CreateModel(
            name='purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('unit_price', models.IntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('raw_material_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.raw_materials')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.product_names')),
            ],
        ),
        migrations.CreateModel(
            name='product_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.product_names')),
            ],
        ),
        migrations.CreateModel(
            name='logistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('loading', models.IntegerField()),
                ('off_loading', models.IntegerField()),
                ('transport', models.IntegerField()),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.purchases')),
            ],
        ),
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('expense_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.expense_names')),
                ('expense_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.expense_units')),
            ],
        ),
        migrations.CreateModel(
            name='employment_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('agreed_salary', models.IntegerField()),
                ('salary_start_date', models.DateField()),
                ('salary_end_date', models.DateField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.employee')),
            ],
        ),
        migrations.CreateModel(
            name='advance_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('advance', models.IntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.employee')),
            ],
        ),
    ]
