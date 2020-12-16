from django.db import models


# Create your models here.

class Perfil(models.Model):
    primeiro_nome = models.CharField(max_length=20, blank=True)
    ultimo_nome = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=35, blank=True)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=20, blank=True)
    profissao = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Bem vindo', self.primeiro_nome


class Categoria(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=True)