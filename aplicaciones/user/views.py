from django.core.files.storage import default_storage
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth.views import (
    LoginView,
)
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from aplicaciones.user.models import User
from aplicaciones.user.forms import UserForm


def login(LoginView):
    template_name = 'accounts/login.html'


def logout(request):
    logout(request)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


def is_admin_user(request):
    return request.user.is_admin


class BeginningUser(TemplateView):
    print(is_admin_user)
    template_name = 'users/list_user.html'


class ListUser(ListView):
    model = User
    template_name = 'users/list_user.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


def list_users(request):
    is_admin = request.user.is_admin
    if is_admin:
        no_users = User.objects.count()
        users = User.objects.filter(is_active=True)
        return render(
            request,
            'users/list_user.html',
            {
                'no_users': no_users,
                'users': users
            }
        )
    else:
        return redirect('index')


def new_user(request):
    is_admin = request.user.is_admin
    if is_admin:
        if request.method == "POST":
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect('user:list_user')
        else:
            user_form = UserForm()
        return render(request, 'users/register_user.html', {'user_form': user_form})
    else:
        return redirect('index')


def update_user(request, id):
    is_admin = request.user.is_admin
    if is_admin:
        user = get_object_or_404(User, pk=id)
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
                return redirect('user:list_user')
        else:
            user_form = UserForm(instance=user)
        return render(request, 'users/update_user.html', {'user_form': user_form})
    else:
        return redirect('index')


def update_my_profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    else:
        user_form = UserForm(instance=user)
    return render(request, 'users/update_my_profile.html', {'user_form': user_form})


def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if user:
        user.delete()
    return redirect('user:list_user')

