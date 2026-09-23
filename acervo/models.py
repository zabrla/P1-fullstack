from django.db import models
from datetime import date

class Autor(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Exemplar(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    codigo_registro = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livro.titulo} - Cód: {self.codigo_registro}"

class Membro(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Empréstimo: {self.exemplar.livro.titulo} para {self.membro.nome}"

    @property
    def multa(self):
        valor_diario = 2.00
        if self.data_devolucao_real:
            atraso = (self.data_devolucao_real - self.data_devolucao_prevista).days
            if atraso > 0:
                return atraso * valor_diario
        elif date.today() > self.data_devolucao_prevista:
            atraso = (date.today() - self.data_devolucao_prevista).days
            return atraso * valor_diario
        return 0.00

class Reserva(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva: {self.livro.titulo} por {self.membro.nome}"