from django.urls import path
from . import views

urlpatterns = [
    path('', views.DictHome.as_view(), name='dict_home'),
    path('add-word', views.WordCreateView.as_view(), name='word_create'),
    path('<int:pk>', views.WordDetailView.as_view(), name='word_detail'),
    path('<int:pk>/update-word', views.WordUpdateView.as_view(), name='word_update'),
    path('<int:pk>/delete-word', views.WordDeleteView.as_view(), name='word_delete')
]