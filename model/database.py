import sqlite3

#cria um banco de dados
connection = sqlite3.connect('database.db')

cursor = connection.cursor()
