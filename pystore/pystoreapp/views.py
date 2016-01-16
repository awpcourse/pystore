from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from pystoreapp.models import Product
from pystoreapp.models import UserProfile
from pystoreapp.models import Order
from pystoreapp.models import OrderedProduct
from pystoreapp.forms import UserLoginForm

def home(request):
    if request.method == 'GET':
        form = UserLoginForm()

        products = Product.objects.all()
        context = {
            'form': form,
            'products' : products
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

    orders = Order.objects.filter(user=UserProfile.objects.get(user=request.user))
    order_products = {}

    # for order in orders:
    #     products_assoc = OrderedProduct.objects.filter(order=order)
    #
    #     for assoc in products_assoc:
    #         #product = Product.objects.get(pk=assoc.product)
    #         order_products[order.id] += 0




    context = {
        'profile': profile,
        'orders': orders,

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
    if not request.user.is_authenticated():
        return redirect('index')

    if 'cart' in request.session:
        if request.method == 'POST':
            shipping_address = request.POST['shipping_address']
            billing_address = request.POST['billing_address']
            order = Order(user=UserProfile.objects.get(user=request.user), shipping_address=shipping_address, billing_address=billing_address, status=0, total=float(request.session['total']))
            order.save()
            products = request.session['cart']
            for key, quantity in products.iteritems():
                ordered_product = OrderedProduct(order=order, product=Product.objects.get(pk=key), quantity=quantity)
                ordered_product.save()

            del request.session['cart']
            del request.session['total']
            return redirect('index')
    else:
        return redirect('index')

    context = {'page_title': 'Checkout'}
    return render(request, 'checkout.html', context)


def cart_view(request):
    if request.method == 'GET' and 'cart' in request.session:
        if 'cart' in request.session:
            products_dict = request.session['cart']
            #products = Product.objects.get(pk__in=products_dict.keys)
            total = 0.0
            prod_total = dict()
            prod_prices = dict()
            prod_names = dict()

            products = Product.objects.filter(pk__in=products_dict.keys)

            for product in products:
                print 'ce naiba', products
                total += product.price * products_dict[unicode(product.id)]
                product.products_total = product.price * products_dict[unicode(product.id)]
                product.quantity = products_dict[unicode(product.id)]
                tt = ''

        request.session['total'] = total
        context = {
            'products': products,
            'total': total,
            'ok': True,
            'page_title': 'Cart',
        }
    else:
        context = {
            'ok': False,
        }
    return render(request, 'cart.html', context)

def remove_cart(request, pk):
    if 'cart' in request.session:
        if pk in list(request.session['cart'].keys()):
            request.session['cart'].pop(pk, None)

    return redirect('cart')