from django.contrib import admin

from administrator.forms import UnitGroceriesForm
from administrator.models import (Agenda, UKM, IKM, Document, UnitGroceries,
                                  VariantGroceries, Market, AgenLPG, KiosPupuk, StockItem)
from django.urls import path
from django.shortcuts import render


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('agenda_name', 'agenda_place', 'formatAgendaDateTime', 'agenda_is_publish')
    list_filter = ('agenda_date_time', 'agenda_is_publish')
    search_fields = ('agenda_name',)
    # prepopulated_fields = {
    #     'agenda_name_slug': ('agenda_name',)
    # }
    readonly_fields = ('agenda_name_slug',)
    actions = ('setAgendaToPublished', 'setAgendaUnpublished')
    fields = (
        'agenda_name', 'agenda_name_slug', 'agenda_place', 'agenda_content', 'agenda_date_time', 'agenda_is_publish'
    )

    @admin.action(description='Mark selected agendas as published')
    def setAgendaToPublished(self, request, queryset):
        count = queryset.update(agenda_is_publish=True)
        self.message_user(request, f'{count} agenda have been published successfully')

    @admin.action(description='Mark selected agendas as unpublished')
    def setAgendaUnpublished(self, request, queryset):
        count = queryset.update(agenda_is_publish=False)
        self.message_user(request, f'{count} agenda have been unpublished successfully')

    @admin.display(description='Agenda Date Time')
    def formatAgendaDateTime(self, obj):
        return obj.agenda_date_time.strftime('%d/%m/%y %H:%M:%S')


@admin.register(UKM)
class UKMAdmin(admin.ModelAdmin):
    list_display = ('ukm_name', 'ukm_owner', 'ukm_created')
    list_filter = ('ukm_created',)
    search_fields = ('ukm_name',)
    exclude = ('ukm_name_slug',)


@admin.register(IKM)
class IKMAdmin(admin.ModelAdmin):
    list_display = ('ikm_name', 'ikm_owner', 'ikm_created')
    list_filter = ('ikm_created',)
    search_fields = ('ikm_name',)
    exclude = ('ikm_name_slug',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'document_sector', 'document_created')


@admin.register(UnitGroceries)
class UnitGroceriesAdmin(admin.ModelAdmin):
    list_display = ('unit_groceries_variant', 'unit_groceries_price', 'unit_groceries_created')
    ordering = ["-unit_groceries_created"]
    list_filter = ('unit_groceries_created',)
    search_fields = ['unit_groceries_variant_id__groceries_name']
    list_per_page = 10
    form = UnitGroceriesForm
    add_form_template = 'admin/administrator/unitgroceries/add_form.html'
    change_form_template = 'admin/administrator/unitgroceries/add_form.html'

    class Media:
        css = {
            'all': ['vendor/css/simple-notify.min.css']
        }
        js = ['admin/js/vendor/jquery/jquery.min.js', 'vendor/script/axios.min.js',
              'vendor/script/simple-notify.min.js']

    def get_urls(self):
        default_url = super().get_urls()
        new_url = [path('upload-excel/', self.upload_excel)]

        return default_url + new_url

    def upload_excel(self, request):
        return render(request, 'admin/upload_excel.html')


@admin.register(VariantGroceries)
class VariantGroceriesAdmin(admin.ModelAdmin):
    ordering = ['-groceries_created']
    search_fields = ('groceries_name',)
    list_per_page = 10
    list_display = ['groceries_name', 'groceries_quantity', 'groceries_massa']


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_per_page = 10
    ordering = ['-market_created']
    search_fields = ('market_name',)
    fields = ['market_name', 'market_address']


@admin.register(AgenLPG)
class AgenLPGAdmin(admin.ModelAdmin):
    list_per_page = 10
    ordering = ['-agen_created']
    search_fields = ('agen_name',)
    exclude = ['agen_slug']


@admin.register(KiosPupuk)
class KiosPupukAdmin(admin.ModelAdmin):
    list_per_page = 10
    ordering = ['-kios_created']
    exclude = ['kios_slug']


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_per_page = 10
    ordering = ['-item_created']
    exclude = ['item_slug']
    list_display = ['item_name', 'item_market', 'item_last_stock']
    search_fields = ['item_name', 'item_market']
    readonly_fields = ['item_last_stock']
