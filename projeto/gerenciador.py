def adicionar_tarefa(tarefas, nome_tarefa=""):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("\n1. Adicionar Tarefas:")
    print("\n2. Ver Tarefas:")
    print("\n3. Atualizar Tarefa:")
    print("\n4. Completar Tarefas:")
    print("\n5. Deletar Tarefas completadas:")
    print("\n6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa Finalizado!")