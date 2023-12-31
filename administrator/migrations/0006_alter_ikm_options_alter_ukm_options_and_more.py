# Generated by Django 4.2.3 on 2023-08-17 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_document_alter_ukm_ukm_name_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ikm',
            options={'verbose_name': 'IKM', 'verbose_name_plural': 'IKM'},
        ),
        migrations.AlterModelOptions(
            name='ukm',
            options={'verbose_name': 'UKM', 'verbose_name_plural': 'UKM'},
        ),
        migrations.AlterModelOptions(
            name='unitgroceries',
            options={'verbose_name': 'Unit Groceries', 'verbose_name_plural': 'Unit Groceries'},
        ),
        migrations.AlterField(
            model_name='document',
            name='document_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Crated at'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_detail',
            field=models.TextField(verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to='file/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_sector',
            field=models.CharField(max_length=255, unique=True, verbose_name='Sector'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_image',
            field=models.ImageField(upload_to='images/ikm/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_legality',
            field=models.CharField(max_length=255, verbose_name='Legality'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_name_slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_number_phone',
            field=models.CharField(max_length=15, verbose_name='Number Phone'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_outlet',
            field=models.TextField(verbose_name='Outlet'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_owner',
            field=models.CharField(max_length=255, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_social_media',
            field=models.URLField(blank=True, null=True, verbose_name='Social Media'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_types_product',
            field=models.CharField(max_length=255, verbose_name='Type of Product'),
        ),
        migrations.AlterField(
            model_name='ikm',
            name='ikm_website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='ukm',
            name='ukm_social_media',
            field=models.URLField(blank=True, null=True, verbose_name='Social Media'),
        ),
        migrations.AlterField(
            model_name='ukm',
            name='ukm_website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='unitgroceries',
            name='unit_groceries_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_groceries', to='administrator.variantgroceries'),
        ),
    ]
