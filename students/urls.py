from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.userProfile, name='profile'),
    path('setting/', views.userSetting, name='setting'),
    ##POST request only
    path('password_change/', views.passwordChange, name='pchange'),
    path('edit_profile/', views.editProfile, name='eprofile'),
    #---#
    path('password_reset/', views.forgotPassword, name='reset'),
    path('password_reset_done/', views.passwordResetDone, name='resetDone'),
    
]