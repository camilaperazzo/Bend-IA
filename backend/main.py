from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    dados = request.get_json()

    if 'sampleCodeNumber' in dados and "cellSizeUniformity" in dados and 'cellShapeUniformity' in dados:
        parametro1 = dados["sampleCodeNumber"]
        parametro2 = dados["cellSizeUniformity"]
        parametro3 = dados["cellShapeUniformity"]

        # Lógica de negócio
        resultado = int(parametro2) + int(parametro3)

        percent = 0
        if resultado == 2:
            percent = 50
        elif resultado == 4:
            percent = 90
        else:
            percent = 0

        # Resposta da APIS
        return {
            'sampleCode': parametro1,
            'result': resultado,
            'hitPercentage': percent
        }
    else:
        return {'error': 'Campos inválidos no JSON recebido'}


if __name__=='__main__':
    app.run()
