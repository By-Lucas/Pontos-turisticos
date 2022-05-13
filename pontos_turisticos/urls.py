from django.contrib import admin
from django.urls import path, include

# AS URL DO DJANGO
urlpatterns = [
    path('admin/', admin.site.urls), # ADMIN
    path('', include('plataforma.urls')), # INCLUI A URL DA PLATAFORMA PARA USAR LÁ NO APP MESMO
    path('auth/', include('users.urls')),# INCLUI A URL DOS USERS PARA USAR LÁ NO APP MESMO
]
