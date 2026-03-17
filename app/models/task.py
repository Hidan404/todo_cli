import sqlite3
from datetime import datetime
from pathlib import Path


class Task:
    def __init__(self, titulo, descricao, data_criacao=None, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def caminho_banco(self):
        return Path(__file__).parent.parent / 'database' / 'tarefas.db'

    def criar_tabela(self):
        conn = sqlite3.connect(self.caminho_banco())
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


    def salvar(self):
        self.criar_tabela()
        conn = sqlite3.connect(self.caminho_banco())
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (titulo, descricao, data_criacao)
            VALUES (?, ?, ?)
        ''', (self.titulo, self.descricao, self.data_criacao))

        conn.commit()
        conn.close()


    @staticmethod
    def listar(self):
        conn = sqlite3.connect(self.caminho_banco())
        cursor = conn.cursor()
        resposta = cursor.execute('''
            SELECT titulo, descricao, data_criacao
            from tarefas           
        ''')
        resposta.fetchall()
        conn.close()



