from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.Register, name="register"),
    path('profile/', views.Profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'Users/password_reset.html'), name="password-reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Users/password_reset_done.html'), name="password-reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Users/password_reset_confirm.html'), name="password-reset_confirm"),
]