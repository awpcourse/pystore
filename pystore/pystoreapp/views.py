from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from pystoreapp.models import Product
from pystoreapp.models import UserProfile
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
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product' : product}
        return render(request, 'product_view.html', context)
    elif request.method == 'POST':
        #cart = request.session['cart'];
        # import pdb; pdb.set_trace()
        #request.session['card'] = dict()
        if 'cart' in request.session:
            if pk in request.session['cart']:
                print "+1"

                request.session['cart'][pk] += 1
                print request.session['cart'][pk]
            else:
                print "new"
                request.session['cart'][pk] = 1
        else:
            request.session['cart'] = {
                pk: 1,
            }
            print "new_cart"

        product = Product.objects.get(pk=pk)
        context = {'product' : product}
        return render(request, 'product_view.html', context)
