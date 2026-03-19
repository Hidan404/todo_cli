from  app.services.task_services import TaskServices
import typer


from app.services.task_services import TaskServices
import typer

app = typer.Typer()
services = TaskServices()


@app.command()
def add(titulo: str, descricao: str):
    services.criar_tarefa(titulo, descricao)
    typer.secho(f"Tarefa {titulo} adicionada com sucesso",fg="green")

@app.command()
def ls():
    tarefas = services.listar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa encontrada")

    for t in tarefas:
        typer.secho(f"ID: {t[0]}, TITULO: {t[1]}, DESCRICAO: {t[2]}",fg=typer.colors.CYAN)


if __name__ == "__main__":
    app() 





