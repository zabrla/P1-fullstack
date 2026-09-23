from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Livro, Emprestimo, Reserva
from .forms import LivroForm, EmprestimoForm, ReservaForm
from datetime import date

def lista_livros(request):
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    
    livros = Livro.objects.all()
    
    if q:
        livros = livros.filter(Q(titulo__icontains=q) | Q(autor__nome__icontains=q))
        
    if status == 'disponivel':
        livros = livros.filter(exemplar__disponivel=True).distinct()
    elif status == 'emprestado':
        livros = livros.filter(exemplar__disponivel=False).distinct()

    return render(request, 'acervo/lista.html', {'livros': livros})

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})

def novo_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            if emprestimo.exemplar.disponivel:
                reservas = Reserva.objects.filter(
                    livro=emprestimo.exemplar.livro, 
                    ativa=True
                ).order_by('data_reserva')
                
                if reservas.exists() and reservas.first().membro != emprestimo.membro:
                    return render(request, 'acervo/form.html', {
                        'form': form, 
                        'erro': 'Este livro possui uma fila de reserva e o membro não é o primeiro da fila.'
                    })
                
                emprestimo.exemplar.disponivel = False
                emprestimo.exemplar.save()
                emprestimo.save()
                
                if reservas.exists() and reservas.first().membro == emprestimo.membro:
                    reserva = reservas.first()
                    reserva.ativa = False
                    reserva.save()
                
                return redirect('lista_livros')
            else:
                return render(request, 'acervo/form.html', {
                    'form': form, 
                    'erro': 'O exemplar selecionado não está disponível.'
                })
    else:
        form = EmprestimoForm()
    return render(request, 'acervo/form.html', {'form': form})

def devolucao(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if not emprestimo.data_devolucao_real:
        emprestimo.data_devolucao_real = date.today()
        emprestimo.save()
        emprestimo.exemplar.disponivel = True
        emprestimo.exemplar.save()
    return redirect('lista_livros')

def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = ReservaForm()
    return render(request, 'acervo/form.html', {'form': form})