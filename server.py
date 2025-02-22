from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hola, Flask en Vercel!"

@app.route("/api/generate-password", methods=["GET"])
def generate_password():
    import random
    import string
    length = int(request.args.get("length", 12))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return jsonify({"password": password})

# Para que funcione en Vercel
if __name__ == "__main__":
    app.run(debug=True)