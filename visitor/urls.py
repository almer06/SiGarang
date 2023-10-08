from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path

from visitor import views

app_name = 'visitor'
urlpatterns = [
    path('', views.HargaSembako.as_view(), name='harga_sembako'),
    path('ukm/', views.UKMVisitor.as_view(), name='ukm'),
    path('ukm/<slug:slug>/', views.UKMDetailVisitor.as_view(), name='ukm-detail'),
    path('ikm/', views.IKMVisitor.as_view(), name='ikm'),
    path('ikm/<slug:slug>/', views.IKMDetailVisitor.as_view(), name='ikm-detail'),
    path('agenda/', views.AgendaVisitor.as_view(), name='agenda'),
    path('login/', views.LoginVisitor.as_view(), name='login'),
    path('register/', views.RegisterVisitor.as_view(), name='register'),
    path('logout/', views.LogoutVisitor.as_view(), name='logout'),
    path('document/', views.DocumentVisitor.as_view(), name='document'),
    path('pasar/', views.PasarView.as_view(), name='pasar'),
    path('sembako/', views.sembako, name='sembako'),
    path('agen-lpg/', views.AgenLPGView.as_view(), name='agen_lpg'),
    path('agen-lpg/<slug:slug>', views.AgenLPGViewDetail.as_view(), name='agen_detail'),
    path('kios-pupuk/', views.KiosPupukListView.as_view(), name='kios_pupuk'),
    path('kios-pupuk/<slug:slug>', views.KiosPupukDetailView.as_view(), name='kios_pupuk_detail'),
    path('stok-barang/', views.StockItemListView.as_view(), name='stock_barang'),
    path('statistic-sembako/', views.dataForStatisticSembako, name='statistic-sembako'),
    path('all-variant/', views.allVariantSembako, name='all-variant-sembako'),
    path('export-excel-sembako/', views.export_excel_harga_sembako, name='excel_sembako'),
    path('import-excel-sembako/', views.import_excel_sembako, name='import_sembako'),
    path('export-excel-ukm', views.export_ukm_to_excel, name='excel_ukm'),
    path('export-ikm-excel/', views.ExportIKMToExcel.as_view(), name='export_ikm_excel'),
    path('export_pasar_excel', views.ExportPasarToExcel.as_view(), name='export_pasar'),
    path('export_agen_excel', views.ExportAgenLPGToExcel.as_view(), name='export_agen'),
    path('export_kios_pupuk_excel', views.ExportKiosPupukToExcel.as_view(), name='export_kios_pupuk'),
    path('export_stok_barang_excel', views.ExportStockItemToExcel.as_view(), name='export_stock_barang'),

    path('reset_password/', views.PasswordResetViewVisitor.as_view(), name='reset_password'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmViewVisitor.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(
        template_name='visitor/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('activate/<uidb64>/<token>', views.ActivateAccount.as_view(), name='active_user')
]
