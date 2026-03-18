from  models.task import Task


class TaskServices():
    def criar_tarefa(self, titulo, descricao):
        nova_tarefa = task = Task(titulo, descricao)
        nova_tarefa.salvar()
        return nova_tarefa


    def listar_tarefas(self):
        return Task.listar()
    
    def verificar_se_tabela_existe(self):
        return Task.verificar_se_tabela_existe()
    
    def deletar_tarefas(self, id):
        return Task.deletar(id)