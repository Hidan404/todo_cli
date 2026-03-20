from app.services.task_services import TaskServices
from typing import Optional

class TaskController:

    def __init__(self):
        self.services = TaskServices()

    def add(self, titulo, descricao, status: Optional[str] = None, prioridade=None, prazo=None):
        self.services.criar_tarefa(titulo, descricao, status=status, prioridade=prioridade, prazo=prazo)
        return f"Tarefa {titulo} adicionada com sucesso"

    def ls(self):
        tarefas = self.services.listar_tarefas()
        return tarefas

    def update(self, id, titulo, descricao, status: Optional[str] = None, prioridade=None, prazo=None):
        self.services.atualizar(id, titulo, descricao, status=status, prioridade=prioridade, prazo=prazo)
        return f"Tarefa {id} atualizada com sucesso"

    def deletar(self, id):
        self.services.deletar_tarefas(id)
        return f"Tarefa {id} deletada com sucesso"


