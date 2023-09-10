# Generated by Django 4.2.3 on 2023-08-09 12:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('agenda_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('agenda_name', models.CharField(max_length=255)),
                ('agenda_place', models.CharField(max_length=255)),
                ('agenda_date_time', models.DateTimeField()),
                ('agenda_content', models.TextField()),
                ('agenda_created', models.DateTimeField(auto_now_add=True)),
                ('agenda_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IKM',
            fields=[
                ('ikm_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ikm_name', models.CharField(max_length=255, unique=True)),
                ('ikm_owner', models.CharField(max_length=255)),
                ('ikm_number_phone', models.CharField(max_length=15)),
                ('ikm_legality', models.CharField(max_length=255)),
                ('ikm_types_product', models.CharField(max_length=255)),
                ('ikm_outlet', models.TextField()),
                ('ikm_address', models.TextField()),
                ('ikm_description', models.TextField()),
                ('ikm_website', models.URLField()),
                ('ikm_social_media', models.URLField()),
                ('ikm_image', models.ImageField(upload_to='images/ikm/')),
                ('ikm_created', models.DateTimeField(auto_now_add=True)),
                ('ikm_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Small and Medium Industry',
                'verbose_name_plural': 'Small and Medium Industry',
            },
        ),
        migrations.CreateModel(
            name='UKM',
            fields=[
                ('ukm_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ukm_name', models.CharField(max_length=255, unique=True)),
                ('ukm_owner', models.CharField(max_length=255)),
                ('ukm_number_phone', models.CharField(max_length=15)),
                ('ukm_legality', models.CharField(max_length=255)),
                ('ukm_types_product', models.CharField(max_length=255)),
                ('ukm_outlet', models.TextField()),
                ('ukm_address', models.TextField()),
                ('ukm_description', models.TextField()),
                ('ukm_website', models.URLField()),
                ('ukm_social_media', models.URLField()),
                ('ukm_image', models.ImageField(upload_to='images/ukm/')),
                ('ukm_created', models.DateTimeField(auto_now_add=True)),
                ('ukm_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Small and Medium Enterprises',
            },
        ),
    ]
