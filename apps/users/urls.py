from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.use_login, name='login' ),
    path('logout/', views.user_logout, name='logout' ),
]
