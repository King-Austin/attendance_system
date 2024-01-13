from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.userProfile, name='profile'),
    path('setting/', views.userSetting, name='setting'),
    path('password_reset/', authViews.PasswordResetView.as_view(), name='forgot'),
    
]