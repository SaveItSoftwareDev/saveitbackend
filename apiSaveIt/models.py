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

    def __str__(self):
        return 'Categoria: {} {}'.format(self.id_utilizador, self.nome)

class SubCategoria(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Sub-Categoria: {} {} {}'.format(self.id_utilizador, self.id_categoria, self.nome)

class Planeamento(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    montante_limite = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    prazo = models.DateField()