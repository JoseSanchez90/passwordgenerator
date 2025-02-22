from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # Renderiza la página HTML

@app.route("/api/generate-password", methods=["GET"])
def generate_password():
    length = int(request.args.get("length", 12))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)