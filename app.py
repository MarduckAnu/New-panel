from flask import Flask, request, jsonify

app = Flask(__name__)
estado = "inicial"

@app.route("/control", methods=["POST"])
def control():
    global estado
    data = request.get_json()
    accion = data.get("accion", "")

    if accion == "encender":
        estado = "encendido"
    elif accion == "apagar":
        estado = "apagado"
    elif accion == "reiniciar":
        estado = "reiniciado"
    else:
        estado = "desconocido"

    print(f"Acción recibida: {accion} -> Estado actual: {estado}")
    return jsonify({"estado": estado})

@app.route("/estado", methods=["GET"])
def get_estado():
    return jsonify({"estado": estado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
