# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm


class LoginPageView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    reverse_url = reverse_lazy('users:login')
