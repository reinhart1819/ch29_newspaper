from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordResetForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChangeView(CreateView):
    form_class: PasswordResetForm
    success_url: reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'