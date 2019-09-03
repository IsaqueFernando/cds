from django.db import models

# Classe responsável pelo modelo do Album
class Album(models.Model):
    nome = models.CharField(max_length=100)
    quant_musicas = models.IntegerField() # Quantidade de músicas por cd.
    ano = models.IntegerField()
    tempo_duracao = models.DurationField() # A inteção é utilizar a duração das músicas e somá-las para obter o tempo total de duração.

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',) # Objeto para ordenação.


# Classe responsável pelo modelo Musica.
class Musica(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE) # Álbum ao qual a música pertence.
    nome = models.CharField(max_length=100)
    duracao = models.DurationField(null=True) # Duração de cada música.
    capa = models.ImageField(upload_to='up_images/') # A inteção é armazenarmos uma imagem de capa e exibirmos o nome da mesma.

    def __str__(self):
        return self.nome

    def get_duracao(): # Obter a duração de uma música.
        return duracao

    class Meta:
        ordering = ('nome',)


# Classe responsável pelo modelo Artista
class Artista(models.Model):
    musica = models.ForeignKey('Musica', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobre = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
