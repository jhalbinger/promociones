from flask import Flask, request, jsonify
import joblib

# Cargar el modelo
modelo = joblib.load("modelo_tree.pkl")

app = Flask(__name__)

@app.route("/promos", methods=["POST"])
def promos():
    datos = request.get_json()
    entrada = [[datos["sexo"], datos["edad"]]]
    prediccion = modelo.predict(entrada)

    if prediccion[0] == 0:
        resultado = "Prefiere supermercado"
    elif prediccion[0] == 1:
        resultado = "Prefiere combustible"
    elif prediccion[0] == 2:
        resultado = "Prefiere gastronomía"
    elif prediccion[0] == 3:
        resultado = "Prefiere pinturería"
    else:
        resultado = "No se puede determinar la preferencia"

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor de promociones activo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

