from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .forms import UserRegisterForm, ProfileEditForm
from .models import Profile
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User

class UserLoginView(LoginView):
    template_name = "users/login.html"
    
    def get_success_url(self):
        return reverse('home')
    
def log_user_out(request):
    logout(request)
    return redirect('login')

class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        pass_text = form.cleaned_data["password"]
        user.set_password(pass_text)
        
        user.save()
        
        Profile.objects.create(user=user)
        
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('login')       
        
def contact(self, request):
    return render(request, "pages/contact.html")

class EditProfile(UpdateView):
    model = User
    template_name = "users/profile_edit.html"
    form_class = ProfileEditForm
    
    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse('home')