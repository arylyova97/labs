from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='services_list'),
    url(r'^services/$', views.ServicesList),
    url(r'^service/(?P<id>\d+)', views.ServicePageView.as_view(), name='service'),
    url(r'login/$', views.login),
    url(r'sign_in/$', views.signUp),
    url(r'logout/$', views.logout),
    url(r'get-services/$',views.get_services),
    url(r'add-service/$',views.add_service),
]