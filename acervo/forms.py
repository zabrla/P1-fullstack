from django import forms
from .models import Livro, Emprestimo, Reserva, Autor
from datetime import date

class LivroForm(forms.ModelForm):
    nome_autor = forms.CharField(max_length=150, label="Nome do Autor")

    class Meta:
        model = Livro
        fields = ['titulo', 'ano']

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano and ano > date.today().year:
            raise forms.ValidationError("O ano de publicação do livro não pode ser um ano futuro.")
        return ano

    def save(self, commit=True):
        livro = super().save(commit=False)
        nome_digitado = self.cleaned_data.get('nome_autor')
        
        autor_obj, created = Autor.objects.get_or_create(nome=nome_digitado)
        livro.autor = autor_obj
        
        if commit:
            livro.save()
        return livro

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['exemplar', 'membro', 'data_emprestimo', 'data_devolucao_prevista']
        widgets = {
            'data_emprestimo': forms.DateInput(attrs={'type': 'date'}),
            'data_devolucao_prevista': forms.DateInput(attrs={'type': 'date'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['livro', 'membro', 'data_reserva', 'ativa']
        widgets = {
            'data_reserva': forms.DateInput(attrs={'type': 'date'}),
        }