from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    signup, login, logout, orders,
    username_password_reset_request, username_password_reset_confirm
)
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),

    path('password_reset/', username_password_reset_request, name='password_reset'),
    path('password_reset_confirm/<int:user_id>/', username_password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]


