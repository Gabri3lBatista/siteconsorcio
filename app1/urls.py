from django.conf.urls.static import static
from django.urls import path
from app1.views import pagina_principal, autenticado, cliente, carro, carro_list, sorteio, logar, deslogar, cadastro, sortear, sobre
from tesi2 import settings

app_name = 'app1'

urlpatterns = [
    path('', pagina_principal),
    path('autenticado', autenticado, name='autenticado'),
    path('cliente', cliente, name='cliente'),
    path('carro', carro, name='carro'),
    path('carro_list', carro_list, name='carro_list'),
    path('sorteio', sorteio, name='sorteio'),
    path('logar', logar, name='logar'),
    path('deslogar', deslogar, name='deslogar'),
    path('cadastro', cadastro, name='cadastro'),
    path('sorteaar', sortear, name='sortear'),
    path('sobre', sobre, name='sobre'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)