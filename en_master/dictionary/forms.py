from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import WordTranslate, Games


class WordForm(forms.ModelForm):
    word = forms.CharField(label='Слово', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'word',
                         'placeholder': 'Слово'
                         }))
    translate = forms.CharField(label='Перевод', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'translate',
                         'placeholder': 'Перевод'
                         }))
    # img = forms.ImageField(label='Фото', 
    #                       widget=forms.FileInput(attrs={
    #                      'class': 'img-for-word',
    #                      'name': 'imgword',
    #                      'placeholder': 'Картинка'
    #                      }))
    # lead_question = forms.CharField(label='Наводящий вопрос', 
    #                  widget=forms.TextInput(attrs={
    #                      'class': 'text',
    #                      'name': 'question',
    #                      'placeholder': 'Наводящий вопрос'
    #                      }))
    
    
    class Meta:
        model = WordTranslate
        fields = ('word', 'translate')
        
        
class GamesForm(forms.ModelForm):
    lead_question = forms.CharField(label='Наводящий вопрос', 
                          widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'question',
                         'placeholder': 'Наводящий вопрос'
                         }))
    
    img = forms.ImageField(label='Фото', 
                          widget=forms.FileInput(attrs={
                         'class': 'img-for-word',
                         'name': 'imgword',
                         'placeholder': 'Картинка'
                         }))
    
    
    class Meta:
        model = Games
        fields = ('lead_question', 'img')


# class ImgGameForm(forms.ModelForm):
#     img = forms.ImageField(label='Фото', 
#                           widget=forms.FileInput(attrs={
#                          'class': 'img-for-word',
#                          'name': 'imgword',
#                          'placeholder': 'Картинка'
#                          }))
    
    
#     class Meta:
#         model = ImgGame
#         fields = ('img',)
        
        
# class WordGameForm(forms.ModelForm):
    # lead_question = forms.CharField(label='Наводящий вопрос', 
    #                  widget=forms.TextInput(attrs={
    #                      'class': 'text',
    #                      'name': 'question',
    #                      'placeholder': 'Наводящий вопрос'
    #                      }))
    
    
#     class Meta:
#         model = WordGame
#         fields = ('lead_question',)