from django.conf.urls import url

from pystoreapp import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/(?P<pk>\d+)$', views.profileDetails, name='profile'),
    # url(r'^cart/$', '', name='cart'),
    # url(r'^products/$', '', name='products'),
    # url(r'^products/(?P<pk>\d+)$', '', name='products_details'),
    # url(r'^checkout/$', '' , name='checkout'),
    #
    # url(r'^register/$', '', name='register'),
    # url(r'^logout/$', '' , name='logout'),
    # url(r'^userpanel/(?P<pk>\d+)$', '' , name='userpanel'),
    url(r'^product/(?P<pk>\d+)/$', views.product_view, name='product_view'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^cart/$', views.cart_view, name='cart'),
    url(r'^remove_cart/(?P<pk>\d+)/$', views.remove_cart, name='remove_cart'),


]
