import tkinter as tk
from tkinter import messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear variables de control para las entradas de fecha, hora y descripción
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.description_var = tk.StringVar()

        # Crear el frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Etiqueta y campo de entrada para la fecha
        self.date_label = tk.Label(self.main_frame, text="Fecha:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.main_frame, textvariable=self.date_var)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora
        self.time_label = tk.Label(self.main_frame, text="Hora:")
        self.time_label.grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = tk.Entry(self.main_frame, textvariable=self.time_var)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción
        self.description_label = tk.Label(self.main_frame, text="Descripción:")
        self.description_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        self.description_entry = tk.Entry(self.main_frame, textvariable=self.description_var, width=50)
        self.description_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=3)

        # Botón para agregar citas
        self.add_button = tk.Button(self.main_frame, text="Agregar Cita", command=self.add_event)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        # ListBox para mostrar las citas
        self.event_listbox = tk.Listbox(self.main_frame, width=80, height=15)
        self.event_listbox.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

        # Botón para ver citas
        self.view_button = tk.Button(self.main_frame, text="Ver Citas", command=self.view_events)
        self.view_button.grid(row=4, column=0, padx=5, pady=5)

        # Botón para eliminar citas
        self.delete_button = tk.Button(self.main_frame, text="Eliminar Cita", command=self.delete_event)
        self.delete_button.grid(row=4, column=1, padx=5, pady=5)

    def add_event(self):
        # Obtener la fecha, hora y descripción ingresadas por el usuario
        date = self.date_var.get()
        time = self.time_var.get()
        description = self.description_var.get()

        # Verificar que se ingresaron fecha, hora y descripción
        if date and time and description:
            # Crear el texto de la cita con la fecha, hora y descripción
            event_text = f"Fecha: {date}, Hora: {time}, Descripción: {description}"
            # Agregar la cita al ListBox
            self.event_listbox.insert(tk.END, event_text)
            # Limpiar los campos de fecha, hora y descripción
            self.date_var.set("")
            self.time_var.set("")
            self.description_var.set("")
        else:
            # Mostrar un mensaje de advertencia si falta alguno de los campos
            messagebox.showwarning("Campos Incompletos", "Por favor ingrese fecha, hora y descripción.")

    def view_events(self):
        # Obtener todas las citas del ListBox
        events = self.event_listbox.get(0, tk.END)
        # Mostrar las citas en un cuadro de diálogo
        messagebox.showinfo("Citas", "\n".join(events))

    def delete_event(self):
        # Obtener el índice de la cita seleccionada en el ListBox
        selected_index = self.event_listbox.curselection()
        # Verificar si se seleccionó una cita
        if selected_index:
            # Eliminar la cita seleccionada del ListBox
            self.event_listbox.delete(selected_index)
        else:
            # Mostrar un mensaje de advertencia si no se seleccionó ninguna cita
            messagebox.showwarning("Ninguna Cita Seleccionada", "Por favor seleccione una cita.")

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = AgendaApp(root)
root.mainloop()