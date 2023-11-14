from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import WordTranslate


class WordForm(forms.ModelForm):
    word = forms.CharField(label='Логин', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'username',
                         'placeholder': 'Логин'
                         }))
    translate = forms.EmailField(label='Почта', 
                     widget=forms.EmailInput(attrs={
                         'class': 'text',
                         'name': 'mail',
                         'placeholder': 'Почта'
                         }))
    img = forms.ImageField(label='Фото', 
                          widget=forms.FileInput(attrs={
                         'class': 'img-for-word',
                         'name': 'imgword',
                         'placeholder': 'Картинка'
                         }))
    lead_question = forms.CharField(label='Наводящий вопрос', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'question',
                         'placeholder': 'Наводящий вопрос'
                         }))
    
    class Meta:
        model = WordTranslate
        fields = ('word', 'translate', 'img', 'lead_question')

