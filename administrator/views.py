from django.shortcuts import render
from django.contrib.auth.views import LoginView, TemplateView


# Create your views here.
class LoginAdmin(LoginView):
    template_name = 'administrator/login.html'


class DashboardView(TemplateView):
    template_name = 'administrator/dashboard.html'
    extra_context = {
        'title': 'Dashboard'
    }
