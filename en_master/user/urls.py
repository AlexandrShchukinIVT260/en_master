from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>', views.UserHome.as_view(), name='user_home'),
    path('sign-up/', views.RegisterUser.as_view(), name='sign_up'),
    path('sign-in/', views.LoginUser.as_view(), name='sign_in'),
    path('sign-out/', views.sign_out_user, name='sign_out'),
    path('<str:slug>/delete-user/', views.DeleteUser.as_view(), name='delete'),
    path('<str:slug>/update-user/', views.UpdateUser.as_view(), name='update'),
    # path('update-user', views.UserUpdateView.as_view(), name='user_update'),
    # path('delete-user', views.UserDeleteView.as_view(), name='user_delete'),
]
