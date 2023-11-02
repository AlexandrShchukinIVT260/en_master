from django.contrib.auth import get_user_model
from uuid import uuid4
from pytils.translit import slugify


User = get_user_model()


menu = [
    {'title': 'Личный кабинет', 'url_name': 'user_home'},
    # {'title': 'Регистрация', 'url_name': 'sign_in'},
    # {'title': 'Вход', 'url_name': 'sign_up'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        context['menu'] = menu
        context['users'] = users
        if 'user_selected' not in context:
            context['user_selected'] = 0
        return context
    

def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug