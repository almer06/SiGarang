from django.urls import path
from administrator.views import LoginAdmin, get_price_sembako_yesterday

app_name = 'administrator'
urlpatterns = [
    path('login/', LoginAdmin.as_view(), name='login'),
    path('price_grocery_yesterday/', get_price_sembako_yesterday, name='price_grocery_yesterday')
]
