
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cadastrar-ponto/', views.cadastrar_ponto_turistico, name='cadastrar'),
    path('deletar-ponto/<int:id>/', views.deletar_ponto_turistico, name='deletar_ponto'),
    path('editar-ponto/<int:id>/', views.editar_ponto_turistico, name='editar_ponto'),
    path('ponto-turistico/<int:id>/', views.ponto_turistico, name='ponto_turistico')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)