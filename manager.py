def add_task(tasks, task_name):
    task = {"task": task_name, "closed": False}
    tasks.append(task)
    print(f"Tarefa '{task_name}' adicionada com sucesso!")

def visualize_tasks(tasks):
    print(f"\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['closed'] else " "
        task_name = task['task']
        print(f"{index}. [{status}] {task_name}")

def update_task_name(tasks, task_index, new_task_name):
    adjusted_index = int(task_index) -1
    if adjusted_index >= 0 and adjusted_index < len(tasks):
        tasks[adjusted_index]['task'] = new_task_name
        print(f"Tarefa {task_index} atualizada para '{new_task_name}'")
    else:
        print("O índice selecionado é inválido!")

def closed_task(tasks, task_index):
    adjusted_index = int(task_index) -1
    if adjusted_index >= 0 and adjusted_index < len(tasks) and tasks[adjusted_index]['closed']:
        print("A tarefa selecionada já foi completada!")
    elif adjusted_index >= 0 and adjusted_index < len(tasks) and tasks[adjusted_index]['closed'] == False:
        tasks[adjusted_index]['closed'] = True
        print(f"Tarefa {task_index} foi completada!")
    else:
        print("O índice selecionado é inválido!")

def delete_closed_tasks(tasks):
    for task in tasks:
        if task['closed']:
            tasks.remove(task)
    print("\nTarefas completadas foram deletadas!")

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
    elif choice == "3":
        visualize_tasks(tasks)
        task_index = input("\nDigite o número da tarefa que deseja atualizar: ")
        new_name = input("Digite o novo nome da tarefa: ")
        update_task_name(tasks, task_index, new_name)
    elif choice == "4":
        visualize_tasks(tasks)
        task_index = input("\nDigite o número da tarefa que deseja completar: ")
        closed_task(tasks, task_index)
    elif choice == "5":
        delete_closed_tasks(tasks)
        visualize_tasks(tasks)
    elif choice == "6":
        break

print("Programa Finalizado!")