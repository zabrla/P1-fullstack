from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.AutorListCreate.as_view(), name='autor-list'),
    path('autores/<int:pk>/', views.AutorRetrieveUpdateDestroy.as_view(), name='autor-detail'),
    
    path('livros/', views.LivroListCreate.as_view(), name='livro-list'),
    path('livros/<int:pk>/', views.LivroRetrieveUpdateDestroy.as_view(), name='livro-detail'),
    
    path('exemplares/', views.ExemplarListCreate.as_view(), name='exemplar-list'),
    path('exemplares/<int:pk>/', views.ExemplarRetrieveUpdateDestroy.as_view(), name='exemplar-detail'),
    
    path('membros/', views.MembroListCreate.as_view(), name='membro-list'),
    path('membros/<int:pk>/', views.MembroRetrieveUpdateDestroy.as_view(), name='membro-detail'),
    
    path('emprestimos/', views.EmprestimoListCreate.as_view(), name='emprestimo-list'),
    path('emprestimos/<int:pk>/', views.EmprestimoRetrieveUpdateDestroy.as_view(), name='emprestimo-detail'),
    
    path('reservas/', views.ReservaListCreate.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', views.ReservaRetrieveUpdateDestroy.as_view(), name='reserva-detail'),
]