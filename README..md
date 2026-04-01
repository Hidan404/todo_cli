# Todo CLI - Gerenciador de tarefas no terminal

Projeto simples de **gerenciamento de tarefas pelo terminal** feito em Python.  
A ideia foi criar uma ferramenta CLI real que pudesse ser instalada no sistema e usada em qualquer pasta do Linux.

Esse projeto também foi feito para **aprender na prática**:

- criação de CLI em Python
- organização de projeto em camadas
- uso de banco de dados
- empacotamento de aplicação Python
- instalação global usando pipx

---

# Tecnologias usadas

- Python 3
- Typer (framework para CLI)
- SQLite
- pipx para instalação global

---

# Estrutura do projeto


todo_cli
│
├── app
│ ├── controllers
│ ├── services
│ ├── models
│ ├── database
│ └── views
│ └── cli.py
│
└── pyproject.toml


O projeto segue uma organização parecida com MVC:


CLI
↓
Controller
↓
Service
↓
Database


---

# Instalação

Primeiro instale o **pipx** (recomendado para instalar CLI Python).

```bash
sudo apt install pipx
pipx ensurepath

Depois entre na pasta do projeto:

cd todo_cli

Instale o CLI:

pipx install .

Agora o comando todo ficará disponível no sistema.

Como usar

Ver ajuda do programa:

todo --help
Comandos disponíveis
Adicionar tarefa
todo add "titulo da tarefa" "descricao da tarefa" --status "pendente" --prioridade "alta" --prazo "2024-12-31"

Exemplo:

todo add "Estudar Python" "Treinar CLI e projetos" --status "pendente"
Listar tarefas

Mostra todas as tarefas salvas.

todo ls
Atualizar tarefa

Permite editar uma tarefa existente.

todo update 1 "novo titulo" "nova descricao" --status "concluida"

O número 1 é o ID da tarefa.

Deletar tarefa

Remove uma tarefa do sistema.

todo deletar 1
Funcionalidades

O CLI permite:

criar tarefas
listar tarefas
atualizar tarefas
remover tarefas
definir prioridade
definir status
definir prazo

Basicamente segue o padrão CRUD:

Create
Read
Update
Delete
Objetivo do projeto

Esse projeto foi feito para praticar desenvolvimento backend em Python e entender melhor:

arquitetura de software
criação de ferramentas de terminal
empacotamento de aplicações
uso de banco SQLite

Também foi um exercício para aprender como ferramentas CLI reais funcionam no Linux.

Melhorias futuras

Algumas melhorias que podem ser adicionadas:

comando todo stats
busca de tarefas
filtro por status
interface mais bonita no terminal
cores e tabelas
exportar tarefas
Autor

Ronald Sousa


---

