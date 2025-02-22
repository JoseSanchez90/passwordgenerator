from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Sirve el HTML

@app.route("/generar", methods=["POST"])
def generar_contraseña():
    data = request.get_json()
    longitud = int(data.get("longitud", 8))  # Longitud por defecto 8

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))

    return jsonify({"contraseña": contraseña})  # Devuelve JSON

if __name__ == "__main__":
    app.run(debug=True)
