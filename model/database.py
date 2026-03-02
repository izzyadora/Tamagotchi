import sqlite3

#cria um banco de dados
def initialize_database():
    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS study_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        start_timestamp INTEGER NOT NULL,
        end_timestamp INTEGER NOT NULL
        );
    """
    cursor.execute(command1)
    connection.commit()