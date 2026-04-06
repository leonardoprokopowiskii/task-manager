def add_task(tasks, task_name):
    task = {"task": task_name, "closed": False}
    tasks.append(task)
    print(f"Tarefa '{task_name}' adicionada com sucesso!")
    return

tasks = []

while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "1":
        task_name = input("\nDigite o nome da tarefa: ")
        add_task(tasks, task_name)
    elif choice == "6":
        break

print("Programa Finalizado!")