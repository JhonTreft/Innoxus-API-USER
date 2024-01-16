from django.urls import path
from .views import *

urlpatterns = [
    path('login', login,name='login user'),
    path('register',register,name='regitser user')
]
