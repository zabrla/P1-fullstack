from rest_framework import serializers
from .models import Autor, Livro, Exemplar, Membro, Emprestimo, Reserva

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor']

class ExemplarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplar
        fields = ['id', 'livro', 'codigo_registro', 'disponivel']

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = ['id', 'nome', 'email']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'exemplar', 'membro', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'livro', 'membro', 'data_reserva', 'ativa']