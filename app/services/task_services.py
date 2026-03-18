from  models.task import Task


class TaskServices():
    def criar_tarefa(self, titulo, descricao):
        self.task = Task(titulo, descricao)
        self.task.salvar()


    def listar_tarefas(self):
        return Task.listar(self.task)
    
    def verificar_se_tabela_existe(self):
        return Task.verificar_se_tabela_existe(self.task)
    
    def deletar_tarefas(self, id):
        return Task.deletar(self.task, id)