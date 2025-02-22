from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)  # Habilita CORS para que el frontend pueda comunicarse con el backend

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generar", methods=["POST"])
def generar():
    data = request.get_json()
    longitud = int(data["longitud"])
    contraseña = generar_contraseña(longitud)
    return jsonify({"contraseña": contraseña})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
