# Generated by Django 4.2.3 on 2023-10-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0011_alter_variantgroceries_groceries_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantgroceries',
            name='groceries_massa',
            field=models.CharField(max_length=64, verbose_name='Satuan Bahan Pokok'),
        ),
        migrations.AlterField(
            model_name='variantgroceries',
            name='groceries_quantity',
            field=models.PositiveSmallIntegerField(verbose_name='Jumlah Bahan Pokok'),
        ),
    ]
