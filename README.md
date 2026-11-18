## Rotas e Endpoints da API

Com o servidor local em execução (`python manage.py runserver`), o projeto fica disponível em `http://127.0.0.1:8000/`.

### Painel Administrativo
* **Admin:** `http://127.0.0.1:8000/admin/`

### API REST (Django REST Framework)
Todos os recursos seguem o padrão REST sob o prefixo `/api/`, suportando listagem e criação (`GET`, `POST`) na rota principal, e consulta, atualização e remoção (`GET`, `PUT`, `PATCH`, `DELETE`) na rota com ID (`<int:pk>`):

| Recurso | Listar / Criar (`GET`, `POST`) | Detalhar / Editar / Apagar (`GET`, `PUT`, `PATCH`, `DELETE`) |
| :--- | :--- | :--- |
| **Autores** | `/api/autores/` | `/api/autores/<id>/` |
| **Livros** | `/api/livros/` | `/api/livros/<id>/` |
| **Exemplares** | `/api/exemplares/` | `/api/exemplares/<id>/` |
| **Membros** | `/api/membros/` | `/api/membros/<id>/` |
| **Empréstimos** | `/api/emprestimos/` | `/api/emprestimos/<id>/` |
| **Reservas** | `/api/reservas/` | `/api/reservas/<id>/` |

Ao acessar qualquer endpoint `/api/.../` diretamente pelo navegador, é possível testar as requisições pela interface navegável (*Browsable API*) do Django REST Framework.
