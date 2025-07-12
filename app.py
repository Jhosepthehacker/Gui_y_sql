import tkinter as tk
import sqlite3 as sql
from tkinter import Menu, messagebox, ttk

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def on_data_base():
    create_data_base()
    create_table()
    insert_data("Pedro", 22, "pedrito1234")
    read_data()
    drop_data()

def create_data_base():
    conn = sql.connect("data_base.db")
    conn.commit()
    conn.close()

def create_table():
    conn = sql.connect("data_base.db")
    cursor = conn.cursor()
    cursor.execute(
      """CREATE TABLE IF NOT EXISTS data(
        name TEXT,
        age INTEGER,
        password TEXT
     )"""
)
    conn.commit()
    conn.close()

def insert_data(name, age, password):
    conn = sql.connect("data_base.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO data VALUES ('{name}', {age}, '{password}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def read_data():
    conn = sql.connect("data_base.db")
    cursor = conn.cursor()
    instruction = "SELECT * FROM data;"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    for i in data:
        name = i[0]
        age = i[1]
        password = i[2]
    see = ["#-------------------#",
               "#   Nombre:         #",
             f"#    {name}          #",
                 "#-------------------#",
                "#     Edad:         #",
               f"#      {age}           #",
                 "#-------------------#",
                 "#  Password:        #",
               f"#  {password}      #",
                 "#-------------------#"
]
    for i in see:
        print(i)

def drop_data():
    conn = sql.connect("data_base.db")
    cursor = conn.cursor()
    drop_data = "DROP TABLE IF EXISTS data;"
    cursor.execute(drop_data)
    conn.commit()
    conn.close()

root = tk.Tk()
root.title("Proyect GUI And Data Base")
root.geometry("400x400")

label = tk.Label(root, text="Hola A Todos", fg="green")
label.pack(pady=10)

button = ttk.Button(root, text="Consulta", command=on_data_base)
button.pack(pady=10)

root.mainloop()
