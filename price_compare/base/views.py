from os import terminal_size
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django. contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.http import HttpResponse
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
def homePage(response):
      return render(response, "base/home.html", {})




