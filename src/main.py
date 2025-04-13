from models.task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n📋 MENU:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            title = input("Título: ")
            desc = input("Descrição: ")
            manager.add_task(title, desc,)

        elif opcao == "2":
            manager.list_tasks()

        elif opcao == "3":
            id_ = int(input("ID da tarefa: "))
            manager.mark_completed(id_)

        elif opcao == "4":
            id_ = int(input("ID da tarefa: "))
            manager.remove_task(id_)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
