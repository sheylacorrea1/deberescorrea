import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        self.resultado = 0.0

        self.etiqueta_num1 = tk.Label(ventana, text="Número 1:")
        self.etiqueta_num1.grid(row=0, column=0, padx=5, pady=5)

        self.etiqueta_num2 = tk.Label(ventana, text="Número 2:")
        self.etiqueta_num2.grid(row=1, column=0, padx=5, pady=5)

        self.etiqueta_resultado = tk.Label(ventana, text="Resultado:")
        self.etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.campo_num1 = tk.Entry(ventana)
        self.campo_num1.grid(row=0, column=1, padx=5, pady=5)

        self.campo_num2 = tk.Entry(ventana)
        self.campo_num2.grid(row=1, column=1, padx=5, pady=5)

        self.boton_sumar = tk.Button(ventana, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(row=3, column=0, padx=5, pady=5)

        self.boton_restar = tk.Button(ventana, text="Restar", command=self.restar)
        self.boton_restar.grid(row=3, column=1, padx=5, pady=5)

        self.boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=self.multiplicar)
        self.boton_multiplicar.grid(row=4, column=0, padx=5, pady=5)

        self.boton_dividir = tk.Button(ventana, text="Dividir", command=self.dividir)
        self.boton_dividir.grid(row=4, column=1, padx=5, pady=5)

        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.boton_salir = tk.Button(ventana, text="Salir", command=self.salir)
        self.boton_salir.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def sumar(self):
        try:
            num1 = float(self.campo_num1.get())
            num2 = float(self.campo_num2.get())
            self.resultado = num1 + num2
            self.etiqueta_resultado.config(text=f"Resultado: {self.resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def restar(self):
        try:
            num1 = float(self.campo_num1.get())
            num2 = float(self.campo_num2.get())
            self.resultado = num1 - num2
            self.etiqueta_resultado.config(text=f"Resultado: {self.resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.campo_num1.get())
            num2 = float(self.campo_num2.get())
            self.resultado = num1 * num2
            self.etiqueta_resultado.config(text=f"Resultado: {self.resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def dividir(self):
        try:
            num1 = float(self.campo_num1.get())
            num2 = float(self.campo_num2.get())
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
            else:
                self.resultado = num1 / num2
                self.etiqueta_resultado.config(text=f"Resultado: {self.resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def limpiar(self):
        self.campo_num1.delete(0, tk.END)
        self.campo_num2.delete(0, tk.END)
        self.etiqueta_resultado.config(text="Resultado:")

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()