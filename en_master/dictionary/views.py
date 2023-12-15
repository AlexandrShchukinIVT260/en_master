from django.utils import timezone
from django.shortcuts import render
from user.models import WordTranslate
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin

from user.utils import *
from .forms import *


class DictHome(LoginRequiredMixin, DataMixin, ListView):
    model = WordTranslate
    template_name = 'dictionary/dictionary.html'
    context_object_name = 'words'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Словарь")
        return dict(list(context.items()) + list(c_def.items()))


class WordDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = WordTranslate
    # form_class = WordForm
    template_name = 'dictionary/detail_word.html'
    context_object_name = 'detail'
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обзор слова")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('dict_home')


class WordCreateView(LoginRequiredMixin, DataMixin, CreateView):
    model = WordTranslate
    form_class = WordForm
    template_name = 'dictionary/add_word.html'
    context_object_name = 'create'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить слово")
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WordCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('dict_home')
    

class WordUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
    model = WordTranslate
    form_class = GamesForm
    # fields = "__all__"
    template_name = 'dictionary/update_word.html'
    context_object_name = 'update'
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновить слово")
        if self.request.POST:
            context['word_translate_form'] = WordForm(self.request.POST, instance=self.request.user)
        else:
            context['word_translate_form'] = WordForm(instance=self.request.user)
        return dict(list(context.items()) + list(c_def.items()))
    
    # def get_success_url(self):
    #     return reverse_lazy('dict_home')


class WordDeleteView(LoginRequiredMixin, DataMixin, DeleteView):
    model = WordTranslate
    template_name = 'dictionary/delete_word.html'
    context_object_name = 'delete'
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить слово")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('dict_home')    

