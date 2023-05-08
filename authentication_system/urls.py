from django.urls import path
from .views import loginPage, logoutPage, regPage


urlpatterns = [
    path('loginPage/', loginPage, name='loginPage'),
    path('regPage/', regPage, name='regPage'),
    path('logoutPage/', logoutPage, name='logoutPage')
]