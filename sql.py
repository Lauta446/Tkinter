import mysql.connector
from mysql.connector import Error

class endpoints():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1", user="root", password="", database="tkinter"
        )
        self.cursor = self.conn.cursor()

    def agregar(self, tabla, data_diccionario):
        columnas = ", ".join(data_diccionario.keys())
        valueSlot = ", ".join(["%s"] * len(data_diccionario))
        sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({valueSlot})"
        self.cursor.execute(sql, tuple(data_diccionario.values()))
        self.conn.commit()

    def eliminar(self, tabla, campo_id, valor_id):
        sql = f"DELETE FROM {tabla} WHERE {campo_id} = %s"
        self.cursor.execute(sql, (valor_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar(self, tabla, data_diccionario, campo_id):
        valor_id = data_diccionario[campo_id]
        set_clause = ", ".join([f"{col} = %s" for col in data_diccionario.keys()])
        sql = f"UPDATE {tabla} SET {set_clause} WHERE {campo_id} = %s"
        valores = tuple(data_diccionario.values()) + (valor_id,)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0