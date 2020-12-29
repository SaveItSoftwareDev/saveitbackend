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
    saldo = models.DecimalField(default=0, max_digits=1000, decimal_places=2, blank=True)
    tipo = models.CharField(max_length=20, blank=False)

    # Falta implementar enumerador

    def __str__(self):
        return 'Conta: {} {} {}'.format(self.id_utilizador, self.nome, self.saldo_inicial, self.tipo)

class Invest(models.Model):
    nome = models.CharField(max_length=20, blank=False)
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    montante = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    numero = models.IntegerField(blank=False)
    data = models.DateField()
    #tipo = models.CharField() ACHO QUE PODEMOS DEIXAR ISTO CAIR

    def __str__(self):
        return 'Investimento: {} {} {}'.format(self.id_utilizador, self.nome, self.montante, self.numero,self.data,self.tipo)

class Registo(models.Model):
    id_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=30, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    montante = models.DecimalField(max_digits=30, decimal_places=2, blank=False)
    data = models.DateField()
    #recorrencia = models.CharField(max_length=30, blank=False) ACHO QUE PODEMOS DEIXAR ISTO CAIR

    def __str__(self):
        return 'Planeamento: {} {} {}'.format(self.id_conta, self.id_utilizador, self.tipo, self.descricao, self.categoria,self.sub_categoria,self.montante, self.data)

class Alert(models.Model):
    id_planeamento = models.ForeignKey(Invest, on_delete=models.CASCADE)
    id_utilizador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30, blank=False)
    dataInicial = models.DateField()
    dataFinal = models.DateField()
    montante = models.DecimalField(max_digits=30, decimal_places=2, blank=False)
    montanteLimite = models.DecimalField(max_digits=30, decimal_places=2, blank=False)

    def __str__(self):
        return 'Alerta: {} {} {}'.format(self.id_planeamento, self.id_utilizador, self.id_categoria, self.id_sub_categoria, self.descricao,
                                          self.dataInicial, self.dataFinal, self.montante, self.montanteLimite)
