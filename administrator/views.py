from datetime import datetime, timedelta

from django.contrib.auth.views import LoginView, TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from administrator.models import UnitGroceries


# Create your views here.
class LoginAdmin(LoginView):
    template_name = 'administrator/login.html'


class DashboardView(TemplateView):
    template_name = 'administrator/dashboard.html'
    extra_context = {
        'title': 'Dashboard'
    }


def get_price_sembako_yesterday(request):
    id_sembako = request.GET.get('id_sembako')

    tanggal_hari_ini = datetime.now().date()
    tanggal_kemarin = tanggal_hari_ini - timedelta(days=1)

    query = UnitGroceries.objects.filter(unit_groceries_variant__groceries_id=id_sembako,
                                         unit_groceries_created=tanggal_kemarin)

    if query.count() == 0:
        return JsonResponse({
            'price': 0
        })

    return JsonResponse({
        'price': query.first().unit_groceries_price
    })
