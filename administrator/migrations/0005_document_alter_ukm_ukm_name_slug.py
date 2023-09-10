# Generated by Django 4.2.3 on 2023-08-12 01:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_ikm_ikm_name_slug_ukm_ukm_name_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document_name', models.CharField(max_length=255, unique=True)),
                ('document_sector', models.CharField(max_length=255, unique=True)),
                ('document_detail', models.TextField()),
                ('document_file', models.FileField(upload_to='file/')),
                ('document_created', models.DateTimeField(auto_now_add=True)),
                ('document_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ukm',
            name='ukm_name_slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Slug'),
        ),
    ]
