from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    dados = request.get_json()

    if 'sampleCodeNumber' in dados and "cellSizeUniformity" in dados and 'cellShapeUniformity' in dados and "agglomerateThickness" in dados and "marginalAdherence" in dados and "oneSizeEpithelialCell" in dados and "nakedCores" in dados and "chromatin" in dados and "normalNucleoli" in dados and "mitosis" in dados:
        sampleCodeNumber = dados["sampleCodeNumber"]
        cellSizeUniformity = dados["cellSizeUniformity"]
        cellShapeUniformity = dados["cellShapeUniformity"]
        agglomerateThickness = dados["agglomerateThickness"]
        marginalAdherence = dados["marginalAdherence"]
        oneSizeEpithelialCell = dados["oneSizeEpithelialCell"]
        nakedCores = dados["nakedCores"]
        chromatin = dados["chromatin"]
        normalNucleoli = dados["normalNucleoli"]
        mitosis = dados["mitosis"]

        # Business Logi

        # API Response
        return {
            'sampleCode': sampleCodeNumber,
            'hitPercentage': 95,
            'result': "Benign",
        }
    else:
        return {'error': 'Campos inválidos no JSON recebido'}


if __name__=='__main__':
    app.run()
