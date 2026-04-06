def add_task(tasks, task_name):
    task = {"task": task_name, "closed": False}
    tasks.append(task)
    print(f"Tarefa '{task_name}' adicionada com sucesso!")
    return

def visualize_tasks(tasks):
    print(f"\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['closed'] else " "
        task_name = task['task']
        print(f"{index}. [{status}] {task_name}")


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
    elif choice == "2":
        visualize_tasks(tasks)
    elif choice == "6":
        break

print("Programa Finalizado!")