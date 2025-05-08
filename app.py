from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Cargar modelo
modelo = joblib.load("modelo_tree.pkl")

@app.route("/promos", methods=["POST"])
def promos():
    datos = request.get_json()
    print("Recibido:", datos)  # Esto lo vas a ver en los logs de Render

    # Verificamos que lleguen bien los datos
    if not datos or "sexo" not in datos or "edad" not in datos:
        return jsonify({"error": "Faltan campos"}), 400

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

