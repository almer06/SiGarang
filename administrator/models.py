import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Agenda(models.Model):
    agenda_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agenda_name = models.CharField(max_length=255)
    agenda_name_slug = models.SlugField(max_length=255, blank=True)
    agenda_place = models.CharField(max_length=255)
    agenda_date_time = models.DateTimeField()
    agenda_content = models.TextField()
    agenda_is_publish = models.BooleanField(_('Is Publish'), default=False)
    agenda_created = models.DateTimeField(auto_now_add=True)
    agenda_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agenda'

    def __str__(self):
        return self.agenda_name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.agenda_name_slug = slugify(self.agenda_name)
        return super().save()


class UKM(models.Model):
    ukm_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ukm_name = models.CharField(_('Name'), max_length=255, unique=True)
    ukm_name_slug = models.SlugField(_('Slug'), max_length=255, blank=True)
    ukm_owner = models.CharField(_('Owner'), max_length=255)
    ukm_number_phone = models.CharField(_('Number Phone'), max_length=15)
    ukm_legality = models.CharField(_('Legality'), max_length=255)
    ukm_types_product = models.CharField(_('Type of Product'), max_length=255)
    ukm_outlet = models.TextField(_('Outlet'))
    ukm_address = models.TextField(_('Address'))
    ukm_description = models.TextField(_('Description'))
    ukm_website = models.URLField(_('Website'), null=True, blank=True)
    ukm_social_media = models.URLField(_('Social Media'), null=True, blank=True)
    ukm_image = models.ImageField(_('Image'), upload_to='images/ukm/')
    ukm_created = models.DateTimeField(auto_now_add=True)
    ukm_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'UKM'
        verbose_name_plural = 'UKM'

    def __str__(self):
        return self.ukm_name

    def save(self, **kwargs):
        self.ukm_name_slug = slugify(self.ukm_name)
        return super().save()


class IKM(models.Model):
    ikm_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ikm_name = models.CharField(_('Name'), max_length=255, unique=True)
    ikm_name_slug = models.SlugField(_('Slug'), max_length=255, blank=True)
    ikm_owner = models.CharField(_('Owner'), max_length=255)
    ikm_number_phone = models.CharField(_('Number Phone'), max_length=15)
    ikm_legality = models.CharField(_('Legality'), max_length=255)
    ikm_types_product = models.CharField(_('Type of Product'), max_length=255)
    ikm_outlet = models.TextField(_('Outlet'))
    ikm_address = models.TextField(_('Address'))
    ikm_description = models.TextField(_('Description'))
    ikm_website = models.URLField(_('Website'), blank=True, null=True)
    ikm_social_media = models.URLField(_('Social Media'), blank=True, null=True)
    ikm_image = models.ImageField(_('Image'), upload_to='images/ikm/')
    ikm_created = models.DateTimeField(auto_now_add=True)
    ikm_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'IKM'
        verbose_name_plural = 'IKM'

    def __str__(self):
        return self.ikm_name

    def save(self, **kwargs):
        self.ikm_name_slug = slugify(self.ikm_name)
        return super().save()


class VariantGroceries(models.Model):
    groceries_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groceries_name = models.CharField(max_length=255, unique=True, verbose_name='Nama Bahan Pokok')
    groceries_created = models.DateTimeField(auto_now_add=True)
    groceries_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nama Bahan Pokok'
        verbose_name_plural = 'Nama Bahan Pokok'

    def __str__(self):
        return self.groceries_name


class UnitGroceries(models.Model):
    unit_groceries_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unit_groceries_variant = models.ForeignKey(VariantGroceries, on_delete=models.CASCADE,
                                               related_name='unit_groceries', verbose_name='Nama Bahan Pokok')
    unit_groceries_massa = models.CharField(max_length=64, verbose_name='Satuan Bahan Pokok')
    unit_groceries_price = models.PositiveIntegerField(verbose_name='Harga Bahan Pokok')
    unit_groceries_quantity = models.PositiveSmallIntegerField(verbose_name='Jumlah Bahan Pokok')
    unit_groceries_created = models.DateField(verbose_name='Hari')
    unit_groceries_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Harga Bahan Pokok'
        verbose_name_plural = 'Harga Bahan Pokok'

    def __str__(self):
        return self.unit_groceries_variant.groceries_name


class Document(models.Model):
    document_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_name = models.CharField(_('Name'), unique=True, max_length=255)
    document_sector = models.CharField(_('Sector'), unique=True, max_length=255)
    document_detail = models.TextField(_('Detail'))
    document_file = models.FileField(_('File'), upload_to='file/')
    document_created = models.DateTimeField(_('Crated at'), auto_now_add=True)
    document_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dokumen'
        verbose_name_plural = 'Dokumen'

    def __str__(self):
        return f"{self.document_sector}-{self.document_name}"

    def delete(self, **kwargs):
        self.document_file.delete()
        super().delete()
