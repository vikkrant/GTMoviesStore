from django.urls import path
from . import views
from .views import register
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.index, name="home.index"),
    path('about', views.about, name='home.about'),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
]
