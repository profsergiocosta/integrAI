from django.urls import path
from apps.gestantes.views import index, gestante, buscar, novo_gestante, deletar_gestante, editar_gestante, avaliacao, detalhes_risco

urlpatterns = [
        path('', index, name='index'),
        path('gestante/<int:gestante_id>', gestante, name='gestante'),

        path('gestante/<int:gestante_id>/cadastrar_questionario/', avaliacao, name='questionario'),


        path ('buscar', buscar, name='buscar'),
        path('novo-gestante', novo_gestante, name='novo_gestante'),
        path('editar-gestante/<int:gestante_id>', editar_gestante, name='editar_gestante'),
        path('deletar-gestante/<int:gestante_id>', deletar_gestante, name='deletar_gestante'),
        path('gestante/<int:gestante_id>/risco/<str:risco>/', detalhes_risco, name='detalhes_risco'),

        #path('filtro/<str:categoria>', filtro, name='filtro'),
]