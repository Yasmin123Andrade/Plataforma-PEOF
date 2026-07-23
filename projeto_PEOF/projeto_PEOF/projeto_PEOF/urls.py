from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app_PEOF import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('conteudos/', views.conteudos, name='conteudos'),
    path('medalhistas/', views.medalhistas, name='medalhistas'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('materiais/', views.materiais, name='materiais'),
    path('contatos/', views.contato, name='contato'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Servir arquivos estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)