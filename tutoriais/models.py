from django.db import models
from django.contrib.auth.models import User


class Tutorial(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    datatempo = models.DateTimeField(auto_now_add=True, blank=True)
    visivel = models.BooleanField(default=True)
    nivel = models.SmallIntegerField()
    autor = models.ForeignKey(User)

    def __str__(self):
        return self.titulo

class Secao(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    posicao = models.PositiveSmallIntegerField()
    datatempo = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = ("id", "tutorial")

    def __str__(self):
        return self.titulo

class Artigo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE)
    secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
    posicao = models.PositiveSmallIntegerField()
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    class Meta:
        unique_together = ("id", "secao")

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome