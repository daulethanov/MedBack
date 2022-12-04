from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

from django.contrib.auth.models import User




def home(request):
    return render(request, 'account/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registr.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

#
# def blog_submit(request):
#     if request.method == 'POST':
#         # model = Blog.objects.all()
#         form = FormSubmit(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             form = FormSubmit
#         return render(request, 'question.html', {'form': form})


# class BlogForm(CreateView):
#     form_class = FormSubmit
#     template_name = 'question.html'
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         form = form.save()
#         login(self.request, form)
#         return redirect('home')




def shop(request):
    return render(request, 'shop.html')

# class Submit(ListView):
#     model = Blog
#     template_name = 'question.html'