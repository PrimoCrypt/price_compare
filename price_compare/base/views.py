from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from . import forms

# Create your views here.

#homepage view
def homePage(request):
    return render(request, 'base/home.html')
#end of homepage view


#user regestration functionality
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'base/register.html', context={'form': form})
#end of user regestration functionality


