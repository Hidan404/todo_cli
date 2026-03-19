import typer
from app.controllers.task_controllers import TaskController

app = typer.Typer()
controller = TaskController()


@app.command()
def add(titulo: str, descricao: str):
    msg = controller.add(titulo, descricao)
    typer.secho(msg, fg=typer.colors.GREEN)


@app.command()
def ls():
    tarefas = controller.ls()

    if not tarefas:
        typer.secho("Nenhuma tarefa encontrada", fg=typer.colors.YELLOW)
        return

    for t in tarefas:
        typer.secho(
            f"ID: {t[0]}, TITULO: {t[1]}, DESCRICAO: {t[2]}",
            fg=typer.colors.CYAN
        )


@app.command()
def update(id: int, titulo: str, descricao: str):
    try:
        msg = controller.update(id, titulo, descricao)
        typer.secho(msg, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Erro: {e}", fg=typer.colors.RED)


@app.command()
def deletar(id: int):
    try:
        msg = controller.deletar(id)
        typer.secho(msg, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Erro: {e}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()