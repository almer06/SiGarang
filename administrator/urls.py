from django.urls import path
from administrator.views import LoginAdmin, DashboardView

app_name = 'administrator'
urlpatterns = [
    path('login/', LoginAdmin.as_view(), name='login'),
]
