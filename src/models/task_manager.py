from models.task import Task

class TaskManager:

    # inicio uma lista para armazenar as taferas
    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id = 1

    # adiciono uma nova tarefa a lista
    def add_task(self, title: str, description: str):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1

    # listo as tarefas da lista
    def list_tasks(self):
        for task in self.tasks:
            print(task)

    # removo um item da lista de tarefas
    def remove_task(self, task_id: int):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    # marco como comcluída uma terefa e se por acaso ela nao for achada me retorna uma mensagem de erro.
    def mark_completed(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_completed()
                break
            else:
                print(f"Tarefa com id {task_id} não encontrada.")