# Generated by Django 3.0.2 on 2020-02-05 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AngPricesAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_number', models.CharField(blank=True, max_length=255, null=True)),
                ('oem_number', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=3072, null=True)),
                ('stock', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('kratnost', models.CharField(blank=True, max_length=100, null=True)),
                ('car', models.CharField(blank=True, max_length=255, null=True)),
                ('category_id', models.IntegerField()),
                ('subcategory_id', models.IntegerField(blank=True, null=True)),
                ('supplier', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ang_prices_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AngSuppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('folder', models.CharField(max_length=255)),
                ('supplier_file1', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('period_price_days', models.IntegerField()),
                ('delivery_days', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('email2', models.CharField(blank=True, max_length=255, null=True)),
                ('price_orig_number', models.CharField(blank=True, max_length=5, null=True)),
                ('price_oem_number', models.CharField(max_length=5)),
                ('price_brand', models.CharField(max_length=5)),
                ('price_name', models.CharField(max_length=5)),
                ('price_stock', models.CharField(max_length=5)),
                ('price_price', models.CharField(max_length=5)),
                ('price_kratnost', models.CharField(max_length=4)),
                ('price_notes', models.CharField(max_length=5)),
                ('delimeter', models.CharField(blank=True, max_length=17, null=True)),
                ('empty_fields', models.CharField(blank=True, max_length=100, null=True)),
                ('price_table', models.CharField(blank=True, max_length=199, null=True)),
                ('enabled', models.SmallIntegerField()),
                ('enabled_search', models.CharField(max_length=1)),
                ('weight', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'ang_suppliers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BrandsDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'brands_dict',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BrandDictSup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ang_brand', models.CharField(max_length=255, null=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.BrandsDict')),
            ],
            options={
                'managed': True,
            },
        ),
    ]