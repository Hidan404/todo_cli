from app.services.task_services import TaskServices


class TaskController:

    def __init__(self):
        self.services = TaskServices()

    def add(self, titulo, descricao):
        self.services.criar_tarefa(titulo, descricao)
        return f"Tarefa {titulo} adicionada com sucesso"

    def ls(self):
        tarefas = self.services.listar_tarefas()
        return tarefas

    def update(self, id, titulo, descricao):
        self.services.atualizar(id, titulo, descricao)
        return f"Tarefa {id} atualizada com sucesso"

    def deletar(self, id):
        self.services.deletar_tarefas(id)
        return f"Tarefa {id} deletada com sucesso"


