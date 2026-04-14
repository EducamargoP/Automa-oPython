import csv
import os
from datetime import datetime, timedelta

def leitura_arquivo(file_path: str) -> list:
    """Ler tarefas de um arquivo CSV e retornar uma lista de dicionários"""
    tasks = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            task = {
                "id": row["id"],
                "descricao": row["descricao"],
                "data_vencimento": row["data_vencimento"]
            }
            tasks.append(task)

    # Mostrar todas as tarefas lidas
    print("\nLista de tarefas:\n")
    for t in tasks:
        print(f"ID {t['id']} - {t['descricao']} (vence em {t['data_vencimento']})")

    return tasks


def verificar_vencimentos(tasks: list, dias_alerta: int = 3) -> list:
    """Filtra tarefas que vencem em até X dias"""
    hoje = datetime.today().date()
    proximas = []
    for task in tasks:
        vencimento = datetime.strptime(task["data_vencimento"], "%Y-%m-%d").date()
        if vencimento <= hoje + timedelta(days=dias_alerta):
            proximas.append(task)
    return proximas


def notificar_tarefas(tasks: list) -> None:
    """Exibe notificações no terminal"""
    print("\nTarefas próximas do vencimento:\n")
    for task in tasks:
        print(f"[NOTIFICAÇÃO] Tarefa {task['id']}: {task['descricao']} - Vence em {task['data_vencimento']}")


if __name__ == "__main__":
    arquivo = "tasks.csv"

    if not os.path.exists(arquivo):
        print("Arquivo de tarefas não encontrado!")
    else:
        tarefas = leitura_arquivo(arquivo)  # lê e mostra todas
        proximas = verificar_vencimentos(tarefas)  # filtra vencimentos

        if proximas:
            notificar_tarefas(proximas)
        else:
            print("\nNenhuma tarefa próxima do vencimento.")
