
from os import terminal_size
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django. contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from . import forms


# Create your views here.
class PasswordResetView(PasswordResetView):
    email_termplate_name ='registration/password_reset_email.html'
    form_class = PasswordResetForm
    response_class = 'django.template.response.TemplateResponse'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    title = gettext_lazy('password reset')
    token_generator = 'PasswordResetTokenGenerator'


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


