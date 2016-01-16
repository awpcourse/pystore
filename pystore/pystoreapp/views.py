from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

def homeView(request):
    if request.method == 'GET':
        nume_var = "Mama are mere"
        context = {'nume' : nume_var}
        return render(request, 'login.html', context)




