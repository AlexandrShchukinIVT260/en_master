from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'username',
                         'placeholder': 'Логин'
                         }))
    email = forms.EmailField(label='Почта', 
                     widget=forms.EmailInput(attrs={
                         'class': 'text',
                         'name': 'mail',
                         'placeholder': 'Почта'
                         }))
    password1 = forms.CharField(label='Пароль', 
                          widget=forms.PasswordInput(attrs={
                         'class': 'text',
                         'name': 'password1',
                         'placeholder': 'Пароль'
                         }))
    password2 = forms.CharField(label='Повторить пароль', 
                          widget=forms.PasswordInput(attrs={
                         'class': 'text',
                         'name': 'password2',
                         'placeholder': 'Повторить пароль'
                         }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', 
                     widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'username',
                         'placeholder': 'Логин'
                         }))
    password = forms.CharField(label='Пароль', 
                          widget=forms.TextInput(attrs={
                         'class': 'text',
                         'name': 'password1',
                         'placeholder': 'Пароль'
                         }))


class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления данных пользователя
    """
    username = forms.CharField(label='Логин', 
                     widget=forms.TextInput(attrs={
                        #  'class': 'text',
                        #  'name': 'username',
                         'placeholder': 'Логин'
                         }))
    email = forms.EmailField(label='Почта', 
                     widget=forms.EmailInput(attrs={
                        #  'class': 'text',
                        #  'name': 'mail',
                         'placeholder': 'Почта'
                         }))
    first_name = forms.CharField(label='Имя', 
                          widget=forms.TextInput(attrs={
                        #  'class': 'text',
                        #  'name': 'password1',
                         'placeholder': 'Имя'
                         }))
    last_name = forms.CharField(label='Фамилия', 
                          widget=forms.TextInput(attrs={
                        #  'class': 'text',
                        #  'name': 'password2',
                         'placeholder': 'Фамилия'
                         }))
    

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        return email


class ProfileUpdateForm(forms.ModelForm):
    """
    Форма обновления данных профиля пользователя
    """
    birth_date = forms.DateField(label='Дата рождения', 
                          widget=forms.DateInput(attrs={
                         'class': 'date',
                         'name': 'birth_date',
                         'placeholder': 'Дата рождения'
                         }))
    avatar = forms.ImageField(label='Фото', 
                          widget=forms.FileInput(attrs={
                         'class': 'img-avatar',
                         'name': 'avatar',
                         'placeholder': 'Фото'
                         }))
    
    
    class Meta:
        model = Profile
        fields = ('slug', 'birth_date', 'avatar')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы обновления
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })