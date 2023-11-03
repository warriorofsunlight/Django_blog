from django.urls import path, include
from .views import register, profile, OtherProfileView
from django.contrib.auth import views
from django.conf.urls.static import static
from users import views as userview
from django.conf import settings

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('<int:pk>/', OtherProfileView.as_view(), name='others'),
    path('password-reset/',
         views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/<uidb64>/<token>/',
         views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

