from models.task import Task

class TaskServices():
    def criar_tarefa(self, titulo, descricao):
        nova_tarefa = Task(titulo, descricao)
        nova_tarefa.salvar()
        return nova_tarefa

    def listar_tarefas(self):
        task = Task("", "")
        return task.listar()
    
    def verificar_se_tabela_existe(self):
        task = Task("", "")
        return task.verificar_se_tabela_existe()
    
    def deletar_tarefas(self, id):
        task = Task("", "")
        return task.deletar(id)
    
    def atualizar(self, id, titulo, descricao):
        task = Task(titulo, descricao, id=id)
        return task.atualizar()


# forma correta de usar
task = TaskServices()
task.criar_tarefa("Java", "estudar java")