from django.db import models
from django.utils import timezone
# from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from datetime import date, timedelta

from .utils import *


# User = get_user_model()


# class Users(models.Model):
#     name = models.CharField('Имя', max_length=50, default='')
#     mail = models.CharField('Почта', max_length=50, default='')
#     password1 = models.CharField('Пароль', max_length=50, default='')
#     password2 = models.CharField('Пароль', max_length=50, default='')
#     birth_date = models.DateField('Дата рождения', default=timezone.now)
    
#     def __str__(self):
#         return f"{self.name}: {self.mail}"
    
#     # def get_absolute_url(self):
#     #     return f'/news/{self.id}'
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='user/images/avatars/%Y/%m/%d/', 
        # default='user/images/avatars/default.png',
        blank=True,  
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    # bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        """
        Сортировка, название таблицы в базе данных
        """
        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        """
        Возвращение строки
        """
        return self.user.username
    
    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse('user_home', kwargs={'slug': self.slug})


class WordTranslate(models.Model):
    word = models.CharField('Слово', max_length=50, default='')
    translate = models.CharField('Перевод', max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.OneToOneField('ImgGame', on_delete=models.SET_NULL, null=True, blank=True)
    lead_question = models.OneToOneField('WordGame', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.word
    
    def get_absolute_url(self):
        return f'/dictionary/{self.id}'
    
    class Meta:
        verbose_name = 'Слово с переводом'
        verbose_name_plural = 'Слова с переводом'
        
    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse('dictionary')
        
        
class ImgGame(models.Model):
    img = models.ImageField(
        verbose_name='Картинка для ImgGame',
        upload_to='user/images/ImgGame/%Y/%m/%d/', 
        # default='user/images/avatars/default.png',
        blank=True,  
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    
    def __str__(self):
        return "image"
    
    # def get_absolute_url(self):
    #     return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        
        
class WordGame(models.Model):
    lead_question = models.CharField('Наводящий вопрос', max_length=250, default='')
    
    def __str__(self):
        return self.lead_question
    
    # def get_absolute_url(self):
    #     return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
