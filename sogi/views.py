from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

def main_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/portal/')
    return render(request, 'index.html',
        context_instance=RequestContext(request))

def logout_page(request):
    """
    log users out and redirect them to main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    """
    allows user to create a sogi account
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/portal/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", 
        {'form': form}, context_instance=RequestContext(request))
    
    