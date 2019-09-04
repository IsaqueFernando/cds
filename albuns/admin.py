from django.contrib import admin
from .models import Album
from .models import Musica
from .models import Artista
from albuns.actions import export_as_csv_action # Armazena a ação de exportar como csv.

# Classe responsável pela model admin da classe albuns
class AlbumAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action("Exportar CSV", fields=['nome', 'quant_musicas', 'ano', 'tempo_duracao'])]

# Classe responsável pela model admin da classe musica
class MusicaAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action("Exportar CSV", fields=['album', 'nome', 'duracao'])]

# Classe responsável pela model admin da classe musica
class ArtistaAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action("Exportar CSV", fields=['musica', 'nome', 'sobre'])]

# Colocamos aqui para inserir as classes admin que foram criadas acima.
admin.site.register(Musica, MusicaAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
