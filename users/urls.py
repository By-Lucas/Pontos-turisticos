from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


# AQUI FICA TODO O COMANDO DE URL DO DJANGO, O QUE CADA BOTAO VAI REDENRIZAR NO (TEMPLATE "HTML")
# O name É O QUE É CHAMADO NO HTML, por exemplo src="{% url 'profile_update' %}" É RECONHECIDO ASSIM NO HTML
urlpatterns = [
    path('register/', views.Sign_Up_View, name='register'),
    path('accounts/profile/', views.profileView.as_view(), name='profile'),
    path('accounts/update/', views.ProfileUpdateView.as_view(), name='profile_update'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# AQUI FAZ O APP users UTILIZAR ARQUIVOS ESTATICOS
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
