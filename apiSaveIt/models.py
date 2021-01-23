from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome


class SubCategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return 'Sub-Categoria: {} {} {}'.format(self.id_subcategoria, self.id_categoria, self.nome)


class Planeamento(models.Model):
    id_planeamento = models.AutoField(primary_key=True)
    montante_limite = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    prazo = models.DateField()

    def __str__(self):
        return 'Planeamento: {} {} {}'.format(self.id_planeamento, self.categoria, self.sub_categoria,
                                              self.montante_limite,
                                              self.prazo)


class Conta(models.Model):
    id_conta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False)
    saldo = models.DecimalField(default=0, max_digits=1000, decimal_places=2, blank=True)
    tipo = models.CharField(max_length=20, blank=False)

    # Falta implementar enumerador

    def __str__(self):
        return 'Conta: {} {} {}'.format(self.id_conta, self.nome, self.saldo, self.tipo)


class Invest(models.Model):
    id_invest = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False)
    montante = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    numero = models.IntegerField(blank=False)
    data = models.DateField()

    # tipo = models.CharField() ACHO QUE PODEMOS DEIXAR ISTO CAIR

    def __str__(self):
        return 'Investimento: {} {} {}'.format(self.id_invest, self.nome, self.montante, self.numero, self.data)


class Registo(models.Model):
    id_registo = models.AutoField(primary_key=True)
    id_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=30, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    montante = models.DecimalField(max_digits=30, decimal_places=2, blank=False)
    data = models.DateField()

    # recorrencia = models.CharField(max_length=30, blank=False) ACHO QUE PODEMOS DEIXAR ISTO CAIR

    def __str__(self):
        return 'Planeamento: {} {} {}'.format(self.id_registo, self.id_conta, self.tipo, self.descricao,
                                              self.categoria, self.sub_categoria, self.montante, self.data, Categoria.nome)


class Alert(models.Model):
    id_alert = models.AutoField(primary_key=True)
    id_planeamento = models.ForeignKey(Invest, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30, blank=False)
    dataInicial = models.DateField()
    dataFinal = models.DateField()
    montante = models.DecimalField(max_digits=30, decimal_places=2, blank=False)
    montanteLimite = models.DecimalField(max_digits=30, decimal_places=2, blank=False)

    def __str__(self):
        return 'Alerta: {} {} {}'.format(self.id_alert, self.id_planeamento, self.id_categoria,
                                         self.id_sub_categoria, self.descricao,
                                         self.dataInicial, self.dataFinal, self.montante, self.montanteLimite)
