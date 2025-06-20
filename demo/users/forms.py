from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'phone', 'email']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
