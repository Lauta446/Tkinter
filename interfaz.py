import tkinter as tk

root = tk.Tk()
root.title("Interfaz CRUD")
root.geometry("500x400")
root.configure(bg="white")

class generica():
    def __init__(self, campos):
        self.campos = campos
        self.referencia = {}

        for i, c in enumerate(self.campos):
            label = tk.Label(root, text=f"{c}", bg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)

            self.referencia[c] = entry

        btn_row = len(self.campos)
        
        self.btn_agregar = tk.Button(root, text="Agregar")
        self.btn_agregar.grid(row=btn_row, column=0, pady=15)

        self.btn_eliminar = tk.Button(root, text="Eliminar")
        self.btn_eliminar.grid(row=btn_row, column=1, pady=15)

        self.btn_modificar = tk.Button(root, text="Modificar")
        self.btn_modificar.grid(row=btn_row, column=2, pady=15)

campos_vehiculo = ["Marca", "Modelo", "Anio", "Patente"]

app = generica(campos_vehiculo)

root.mainloop()