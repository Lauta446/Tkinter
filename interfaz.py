import tkinter as tk

root = tk.Tk()
root.title("Interfaz CRUD")
root.geometry("500x400")
root.configure(bg="white")

class generica():
    def __init__(self, campos, ):
        self.campos = campos
        

        for i, c in enumerate(self.campos):
            label = tk.Label(root, text=f"{c}", bg="white")

            entry = tk.Entry(root)

crearBoton = tk.Button(root, text="Agregar", command="").grid(row=2, column=0)
eliminarBoton = tk.Button(root, text="Eliminar", command="").grid(row=2, column=1)
modificarBoton = tk.Button(root, text="Modificar", command="").grid(row=2, column=2)


root.mainloop()