#!/usr/bin/env python3
import typer
from app.controllers.task_controllers import TaskController

app = typer.Typer()
controller = TaskController()


@app.command()
def add(titulo: str, descricao: str, status: str = typer.Option(None, "--status", "-s"), prioridade: str = typer.Option(None, "--prioridade", "-p"), prazo: str = typer.Option(None, "--prazo", "-d")):
    '''
    python main.py add "titulo da tarefa" "descricao da tarefa" --status "pendente" --prioridade "alta" --prazo "2024-12-31"
    '''
    msg = controller.add(titulo, descricao, status=status, prioridade=prioridade, prazo=prazo)
    typer.secho(msg, fg=typer.colors.GREEN)


@app.command()
def ls():
    '''
    python main.py ls
    '''
    tarefas = controller.ls()

    if not tarefas:
        typer.secho("Nenhuma tarefa encontrada", fg=typer.colors.YELLOW)
        return

    for t in tarefas:
        typer.secho(
            f"ID: {t[0]}, TITULO: {t[1]}, DESCRICAO: {t[2]}, STATUS: {t[3]}, PRIORIDADE: {t[4]}, PRAZO: {t[5]}, DATA DE CRIACAO: {t[6]}",
            fg=typer.colors.CYAN
        )


@app.command()
def update(id: int, titulo: str, descricao: str, status: str = typer.Option(None, "--status", "-s"), prioridade: str = typer.Option(None, "--prioridade", "-p"), prazo: str = typer.Option(None, "--prazo", "-d")):
    '''
    python main.py update 1 "novo titulo" "nova descricao" --status "concluida" --prioridade "baixa" --prazo "2024-11-30"
    '''
    try:
        msg = controller.update(id, titulo, descricao, status=status, prioridade=prioridade, prazo=prazo)
        typer.secho(msg, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Erro: {e}", fg=typer.colors.RED)


@app.command()
def deletar(id: int):
    '''
    python main.py deletar 1
    '''
    try:
        msg = controller.deletar(id)
        typer.secho(msg, fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Erro: {e}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()