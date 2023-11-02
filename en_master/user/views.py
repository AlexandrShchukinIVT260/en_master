from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

from .models import Profile

from .utils import *
from .forms import *


class UserHome(DetailView):
    model = Profile
    template_name = 'user/user_home.html'
    context_object_name = 'profile'
    # queryset = model.objects.all().select_related('user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        return context


class RegisterUser(DataMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user/sign_up_in.html'
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
    
    
class LoginUser(DataMixin, LoginView):
    model = User
    form_class = LoginUserForm
    template_name = 'user/sign_in.html'
    next_page = 'home'
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(c_def.items()))
    
    # def get_success_url(self):
    #     return reverse_lazy('home')


class UpdateUser(UpdateView):
    """
    Представление для редактирования профиля 
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'user/update_user.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(UpdateUser, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('user_home', kwargs={'slug': self.object.slug})
    
    
class DeleteUser(DataMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'user/delete_user.html'
    context_object_name = 'delete'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление пользователя")
        return dict(list(context.items()) + list(c_def.items()))

def sign_out_user(request):
    logout(request)
    return redirect('home')