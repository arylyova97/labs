from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Service


def services_list(request):
    return render(request, 'services/services_list.html', {})


class MainPageView(View):
    def get(self, request):
        data = {
            'top_services': [
                {'title': 'service №1', 'id': 1},
                {'title': 'service №2', 'id': 2},
                {'title': 'service №3', 'id': 3},
            ]
        }
        return render(request, 'services/index.html', data)


class ServicePageView(View):
    def get(self, request, id):
        data = {
            'service': {
                'id': id
            }
        }
        return render(request, 'services/service.html', data)

class ServiceList(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'
