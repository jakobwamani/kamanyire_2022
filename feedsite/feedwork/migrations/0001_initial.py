# Generated by Django 3.2.7 on 2022-07-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('expense', models.CharField(max_length=50)),
                ('supplier', models.CharField(max_length=50)),
                ('unit', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('product', models.CharField(max_length=100)),
                ('maize_bran', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('cotton', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('sun_flower', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('layers_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('shells', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('meat_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('egg_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('fish', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('general_purpose_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('calcium', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('soya_bean', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('animal_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('common_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('brown_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('coconut', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('pig_concentrate', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('wonder_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('big_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('broilers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('chick_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('old_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('growers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('layers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('young_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuantities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('broilers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('chick_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('old_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('growers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('layers_marsh', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('young_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('receipt_number', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('maize_bran', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('cotton', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('sun_flower', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('fish', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('general_purpose_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('layers_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('shells', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('meat_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('egg_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('calcium', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('soya_bean', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('brown_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('animal_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('common_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('pig_concentrate', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('coconut', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('wonder_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('big_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialQuantities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('maize_bran', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('cotton', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('sun_flower', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('fish', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('common_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('general_purpose_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('layers_premix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('shells', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('meat_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('egg_boaster', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('calcium', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('soya_bean', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('brown_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('animal_salt', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('pig_concentrate', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('coconut', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('wonder_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('big_pig', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('raw_material', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
    ]
