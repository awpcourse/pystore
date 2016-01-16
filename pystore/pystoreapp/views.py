from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from pystoreapp.models import UserProfile
from pystoreapp.forms import UserLoginForm

def home(request):
    if request.method == 'GET':
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
    return redirect('profile', pk=pk)


def logout_view(request):
    logout(request)
    return redirect('index')











