def adicionar_tarefa(tarefas, nome_tarefa=""):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa -1

    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice inválido!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa -1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada!")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas!")
    return

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
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o indice da tarefa que deseja atualizar: "))
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o indice da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa Finalizado!")