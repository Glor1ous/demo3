from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from my_app.forms import ApplicationForms
from django.urls import reverse_lazy

# Create your views here.
class ApplicationViems(CreateView):
    form_class = ApplicationForms
    template_name = 'my_app/application.html'
    success_url = reverse_lazy('home')

class Home(TemplateView):
    template_name = 'my_app/home.html'
    success_url = '/success/'