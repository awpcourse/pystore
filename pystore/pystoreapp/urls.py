from django.conf.urls import url

from pystoreapp import views

urlpatterns = [
    url(r'^$', views.homeView, name='login'),
]
