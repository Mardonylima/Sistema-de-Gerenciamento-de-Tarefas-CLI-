class Task:
    # Representa uma tarefa no sistama de Gerenciamento
    def __init__(self, id: int, title: str, description: str  ):

        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        # Marca como comcluída a tarefa
        self.completed = True

    def __str__(self):
        status = 'Concluída' if self.completed else 'Pendente'
        return f"[{status}] {self.id} - {self.title} | {self.description}"