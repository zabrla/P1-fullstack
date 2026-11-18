from rest_framework import generics
from .models import Autor, Livro, Exemplar, Membro, Emprestimo, Reserva
from .serializers import AutorSerializer, LivroSerializer, ExemplarSerializer, MembroSerializer, EmprestimoSerializer, ReservaSerializer

class AutorListCreate(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroListCreate(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class ExemplarListCreate(generics.ListCreateAPIView):
    queryset = Exemplar.objects.all()
    serializer_class = ExemplarSerializer

class ExemplarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exemplar.objects.all()
    serializer_class = ExemplarSerializer

class MembroListCreate(generics.ListCreateAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class MembroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class EmprestimoListCreate(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer