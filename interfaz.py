import tkinter as tk
from tkinter import messagebox


class generica():
    def __init__(self, master, bd, tabla, campos):
        self.master = master
        self.bd = bd
        self.tabla = tabla
        self.campos = campos
        self.referencia = {}

        for i, c in enumerate(self.campos):
            label = tk.Label(self.master, text=f"{c}", bg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)

            self.referencia[c] = entry

        btn_row = len(self.campos)

        self.btn_agregar = tk.Button(self.master, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=btn_row, column=0, pady=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.grid(row=btn_row, column=1, pady=5)

        self.btn_modificar = tk.Button(self.master, text="Modificar", command=self.modificar)
        self.btn_modificar.grid(row=btn_row, column=2, pady=5)

        

    def agarrar(self):
       return {campo: entry.get() for campo, entry in self.referencia.items()}

    def limpiar(self):
        for entry in self.referencia.values():
            entry.delete(0, tk.END)

    def agregar(self):
        data = self.agarrar()
        self.bd.agregar(self.tabla, data)
        messagebox.showinfo("Registro agregado correctamente.")
        self.limpiar()


    def eliminar(self):
        data = self.agarrar()
        campo_id = self.campos[0]
        valor_id = data[campo_id]
        if not valor_id:
            messagebox.showwarning(f"Escriba un {campo_id} para eliminar.")
            return
        eliminado = self.bd.eliminar(self.tabla, campo_id, valor_id)
        if eliminado:
            messagebox.showinfo("Registro eliminado correctamente.")
            self.limpiar()
        else:
            messagebox.showerror(f"El {campo_id} ingresado no existe.")


    def modificar(self):
        data = self.agarrar()
        campo_id = self.campos[0]
        modificado = self.bd.modificar(self.tabla, data, campo_id)
        if modificado:
            messagebox.showinfo("Registro modificado correctamente.")
            self.limpiar()
        else:
            messagebox.showerror("La patente ingresada no existe.")


        
    
