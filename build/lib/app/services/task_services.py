from app.models.task import Task

class TaskServices():
    def criar_tarefa(self, titulo, descricao,status=None, prioridade=None, prazo=None):
        nova_tarefa = Task(titulo, descricao, status=status, prioridade=prioridade, prazo=prazo)
        nova_tarefa.salvar()
        return nova_tarefa

    def listar_tarefas(self):
        return Task.listar()
    
    def verificar_se_tabela_existe(self):
        return Task.verificar_se_tabela_existe()
    
    def deletar_tarefas(self, id):
        return Task.deletar(id)
    
    def atualizar(self, id, titulo, descricao):
        task = Task(titulo, descricao, id=id)
        return task.atualizar()


# forma correta de usar
#task = TaskServices()
#task.criar_tarefa("Java", "estudar java")
#task.criar_tarefa("Ler", "Leitura Diaria")
#task.criar_tarefa("Organizar coleção", "Limpar coleção de mangas e livros")