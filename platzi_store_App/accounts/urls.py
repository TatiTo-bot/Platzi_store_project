from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # URLs de las páginas HTML
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # URLs de la API de autenticación
    path('api/register/', views.register_api, name='api_register'),
    path('api/login/', views.login_api, name='api_login'),
    path('api/logout/', views.logout_api, name='api_logout'),
    path('api/profile/', views.user_profile_api, name='api_profile'),
    path('api/check-username/', views.check_username_api, name='api_check_username'),
]