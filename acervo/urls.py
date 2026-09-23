from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('livro/novo/', views.novo_livro, name='novo_livro'),
    path('emprestimo/novo/', views.novo_emprestimo, name='novo_emprestimo'),
    path('emprestimo/<int:emprestimo_id>/devolucao/', views.devolucao, name='devolucao'),
    path('reserva/nova/', views.nova_reserva, name='nova_reserva'),
]