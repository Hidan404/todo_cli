import sqlite3
from datetime import datetime
from pathlib import Path


class Task:
    def __init__(self, titulo, descricao, data_criacao=None, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def caminho_banco():
        return Path(__file__).parent.parent / 'database' / 'tarefas.db'


    @staticmethod
    def criar_tabela():
        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                data_criacao TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def salvar():
        Task.criar_tabela()
        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, data_criacao)
            VALUES (?, ?, ?)
        ''', (Task.titulo, Task.descricao, Task.data_criacao))
        conn.commit()
        conn.close()

    @staticmethod
    def verificar_se_tabela_existe():
        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='tarefas'
        """)
        tabela_nome = cursor.fetchone()

        if tabela_nome:
            conn.close()
            return True
        else:
            Task.criar_tabela()
            conn.close()
            return False

    @staticmethod
    def deletar(Task, id):
        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar():
        if Task.id is None:
            print("Tarefa precisa de um ID para atualizar")
            return

        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tarefas 
            SET titulo = ?, descricao = ?
            WHERE id = ?
        ''', (Task.titulo, Task.descricao, Task.id))

        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = sqlite3.connect(Task.caminho_banco())
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, titulo, descricao, data_criacao
            FROM tarefas
        ''')
        dados = cursor.fetchall()
        conn.close()
        return dados