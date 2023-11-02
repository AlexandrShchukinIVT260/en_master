from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        # 'values': ['some', 'hello', '123'],
        # 'obj': {
        #     'car': 'BMW',
        #     'age': 18,
        #     'hobby': 'football'
        # }
    }
    return render(request, 'main/index.html', data)
