from django.urls import path

from my_app.views import ApplicationViems, Home

app_name = 'my_app'

urlpatterns = [
    path('application/', ApplicationViems.as_view(), name='application'),
    path('home/', Home.as_view(), name='home'),
]
