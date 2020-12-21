from django.db import models


# Create your models here.

class Perfil(models.Model):
    primeiro_nome = models.CharField(max_length=20, blank=False)
    ultimo_nome = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=35, blank=False)
    idade = models.IntegerField(blank=True)
    cidade = models.CharField(max_length=20, blank=True)
    profissao = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Bem vindo', self.primeiro_nome


class Categoria(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome


class SubCategoria(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return 'Sub-Categoria: {} {} {}'.format(self.id_utilizador, self.id_categoria, self.nome)


class Planeamento(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    montante_limite = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    prazo = models.DateField()

    def __str__(self):
        return 'Planeamento: {} {} {}'.format(self.id_utilizador, self.categoria, self.nome, self.montante_limite,
                                              self.prazo)


class Conta(models.Model):
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=False)
    saldo_inicial = models.DecimalField(default=0, max_digits=1000, decimal_places=2, blank=True)
    tipo = models.CharField(max_length=20, blank=False)

    # Falta implementar enumerador

    def __str__(self):
        return 'Conta: {} {} {}'.format(self.id_utilizador, self.nome, self.saldo_inicial, self.tipo)
