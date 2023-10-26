from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    success_url = reverse_lazy("login")
    template_name = 'signup.html'

    form_class = UserCreationForm
