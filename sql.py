import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )   
    cursor = conexion.cursor()
    print("Conectado")
except Error as error:
    print(f"Hubo un error {error}")

class endpoints():
    def __init__(self):
        pass