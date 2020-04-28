from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class RegisterView(CreateView):
	form_class=UserCreationForm
	template_name='register.html'
	success_url='user:login'