import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Añadir tarea", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.complete_button = tk.Button(self.root, text="Completar tarea (C)", command=self.complete_task)
        self.complete_button.grid(row=1, column=2, padx=5, pady=5)

        self.incomplete_button = tk.Button(self.root, text="Incompleta tarea (D)", command=self.incomplete_task)
        self.incomplete_button.grid(row=2, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.grid(row=3, column=2, padx=5, pady=5)

        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())
        self.root.bind("c", lambda event: self.complete_task())
        self.root.bind("d", lambda event: self.incomplete_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"name": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()

    def incomplete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = False
            self.update_task_list()

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_listbox.insert(tk.END, "✔️ " + task["name"])
                self.task_listbox.itemconfig(tk.END, {'fg': 'green'})
            else:
                self.task_listbox.insert(tk.END, "❌ " + task["name"])
                self.task_listbox.itemconfig(tk.END, {'fg': 'red'})

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()