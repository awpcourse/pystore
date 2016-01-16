from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from pystoreapp.models import Product
from pystoreapp.models import UserProfile
from pystoreapp.models import Order
from pystoreapp.forms import UserLoginForm

def home(request):
    if request.method == 'GET':
        nume_var = "Mama are mere"
        context = {'nume' : nume_var}
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
        else:
            login(request, user)

        return redirect('index')

@login_required
def profileDetails(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    context = {
        'profile': profile

    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'product' : product, 'page_title': product.name}
        return render(request, 'product_view.html', context)
    elif request.method == 'POST':

        if 'cart' in request.session:
            if pk in request.session['cart']:

                request.session['cart'][pk] += 1
            else:

                request.session['cart'][pk] = 1
        else:
            request.session['cart'] = {
                pk: 1,
            }


        product = Product.objects.get(pk=pk)
        context = {'product' : product, 'added': True, 'page_title': product.name }
        return render(request, 'product_view.html', context)

def checkout(request):
    # if not request.session.total:
    #     redirect('cart')
    if request.method == 'POST':
        shipping_address = request.POST['shipping_address']
        billing_address = request.POST['billing_address']
        order = Order(user=UserProfile.objects.get(pk=request.user.id), shipping_address=shipping_address, billing_address=billing_address, status=0, total=0.0)
        order.save()

    context = {'page_title': 'Checkout'}
    return render(request, 'checkout.html', context)