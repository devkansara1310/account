from django.urls import path
from . import views
from .views import registration,login

urlpatterns = [
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
]