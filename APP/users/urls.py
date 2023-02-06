from django.urls import re_path
from . import views

urlpatterns = [
    re_path('login/', views.user_login, name='login'),   
    re_path('profile/', views.profile, name='profile'), 
    re_path('logout/', views.user_logout, name='logout'),
]
