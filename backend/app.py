import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = "airplanes.db"

# 📌 Función para conectar a la base de datos
def conectar_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Para devolver resultados como diccionarios
    return conn

# 📌 Crear la tabla si no existe
def crear_tabla():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aviones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                aerolinea TEXT NOT NULL,
                capacidad INTEGER NOT NULL
            )
        ''')
        conn.commit()

@app.route("/")
def main():
    app.config["DEBUG"] = True
    app.run()


@app.route('/inicio')
def inicio():
    return f"Hola, bienvenido"


if __name__ == "__main__":
    main()