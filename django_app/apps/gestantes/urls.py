from django.urls import path
from apps.gestantes.views import index, lista_gestantes, gestante, buscar, nova_gestante, deletar_gestante, editar_gestante, avaliacao, detalhes_risco, chat, evolucao_riscos_gestante, feed_gestante

urlpatterns = [
        path('', index, name='index'),

        path('lista_gestantes', lista_gestantes, name='lista_gestantes'),

        path('chat', chat, name='chat'),

        path('gestante/<int:gestante_id>', gestante, name='gestante'),

        path('gestante/<int:gestante_id>/cadastrar_questionario/', avaliacao, name='questionario'),


        path ('buscar', buscar, name='buscar'),
        path('nova-gestante', nova_gestante, name='nova_gestante'),
        path('editar-gestante/<int:gestante_id>', editar_gestante, name='editar_gestante'),
        path('deletar-gestante/<int:gestante_id>', deletar_gestante, name='deletar_gestante'),
        path('gestante/<int:gestante_id>/risco/<str:risco>/', detalhes_risco, name='detalhes_risco'),
        #path('gestante/<int:gestante_id>/risco/<slug:slug>/', detalhes_risco, name='detalhes_risco'),
        
        path('gestante/<int:id>/feed/', feed_gestante, name='feed_gestante'),


        path('gestante/<int:gestante_id>/evolucao_riscos/', evolucao_riscos_gestante, name='evolucao_riscos'),


        #path('filtro/<str:categoria>', filtro, name='filtro'),
]