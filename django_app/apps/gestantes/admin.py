from django.contrib import admin

from apps.gestantes.models import Gestante, Avaliacao


admin.site.site_header = "Administrador do Site"  # Título do cabeçalho
admin.site.site_title = "Administração do Meu Site"  # Título na aba do navegador
admin.site.index_title = "Bem-vindo ao Painel de Controle"  # Título na página inicial do admin


class ListandoGestante(admin.ModelAdmin):
    #list_display = ("id", "nome", "sexo", "idade","foto")
    list_display = ("id", "nome", "idade","foto")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    #list_filter = ("sexo",)
    list_editable = ( "foto", )
    #list_editable = ("sexo","idade", "foto")
    list_per_page = 10

admin.site.register(Gestante, ListandoGestante)


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'gestante', 'data_aplicacao', 'peso_atual')
    search_fields = ('gestante__nome', 'peso_atual')
    list_filter = ('data_aplicacao',)