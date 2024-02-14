from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
]
