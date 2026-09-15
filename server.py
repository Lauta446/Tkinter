import tkinter as tk
from sql import endpoints
from interfaz import generica

if __name__ == "__main__":
  
    root = tk.Tk()
    root.title("Sistema CRUD generico")
    root.geometry("450x300")
    root.configure(bg="white")

   
    bd = endpoints()
    tabla_nombre = "propietarios"
    campos_vehiculo = ["dni", "nombre", "apellido", "fecha_compra", "email"]


    app = generica(root, bd, tabla=tabla_nombre, campos=campos_vehiculo)


    root.mainloop()
