from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import MyLoginForm

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.LoginView.as_view(),name = 'login'),
    path('Search_Result/',views.Search_Result, name='Search_Result'),
    path('Post-detail/<int:pk>/',views.Post_Detail, name='Post_Detail'),
]