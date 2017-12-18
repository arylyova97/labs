from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='services_list'),
    url(r'^services/$', views.ServiceList.as_view()),
    url(r'^service/(?P<id>\d+)', views.ServicePageView.as_view(), name='service'),
    url(r'login/$', views.login),
    url(r'sign_in/$', views.signUp),
    url(r'logout/$', views.logout),
]