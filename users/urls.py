from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/', views.verify, name='verify'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]
