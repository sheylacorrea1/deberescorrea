import tkinter as tk


class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista para almacenar las tareas
        self.tareas = []

        # Entrada de texto para añadir nuevas tareas
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=5, pady=5)

        # Botón para añadir tarea
        self.btn_anadir = tk.Button(root, text="Añadir Tarea", command=self.anadir_tarea)
        self.btn_anadir.grid(row=0, column=1, padx=5, pady=5)

        # Lista para mostrar las tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=15)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Vincular la tecla Enter para añadir tarea
        self.entry_tarea.bind("<Return>", self.anadir_tarea_enter)

        # Botón para marcar tarea como completada
        self.btn_completada = tk.Button(root, text="Completada", command=self.marcar_completada)
        self.btn_completada.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Botón para eliminar tarea seleccionada
        self.btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    def anadir_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)

    def anadir_tarea_enter(self, event):
        self.anadir_tarea()

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista_tareas.get(index)
            tarea_completada = tarea + " (Completada)"
            self.lista_tareas.delete(index)
            self.lista_tareas.insert(index, tarea_completada)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.lista_tareas.delete(index)
            del self.tareas[index]


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()


