import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = "airplanes.db"

@app.route("/")
def main():
    app.config["DEBUG"] = True
    app.run()


@app.route('/inicio')
def inicio():
    return f"Hola, bienvenido"


if __name__ == "__main__":
    main()