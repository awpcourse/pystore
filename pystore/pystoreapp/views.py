from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from pystoreapp.models import Product

def home(request):
    if request.method == 'GET':
        nume_var = "Mama are mere"
        context = {'nume' : nume_var}
        return render(request, 'index.html', context)


def product_view(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product' : product}
        return render(request, 'product_view.html', context)
    elif request.method == 'POST':
        #cart = request.session['cart'];

        #request.session['card'] = dict()
        if 'cart' in request.session:
            if(pk in request.session['cart']):
                request.session['cart'][pk.encode('ascii', 'ignore')] = request.session['cart'][pk.encode('ascii', 'ignore')] + 1
            else:
                request.session['cart'][pk.encode('ascii', 'ignore')] = 1
        else:
            request.session['cart'] = dict([(pk.encode('ascii', 'ignore'), 1)])

        product = Product.objects.get(pk=pk)
        context = {'product' : product, 'cart': request.session['cart']}
        return render(request, 'product_view.html', context)
