from django.contrib import admin
from .models import Autor, Livro, Exemplar, Membro, Emprestimo, Reserva

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Exemplar)
admin.site.register(Membro)
admin.site.register(Emprestimo)
admin.site.register(Reserva)