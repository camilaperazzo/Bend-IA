from flask import Flask, request
from flask_cors import CORS
import json
import predict as pred

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.get_json()

    if 'sampleCodeNumber' in data and "cellSizeUniformity" in data and 'cellShapeUniformity' in data and "agglomerateThickness" in data and "marginalAdherence" in data and "oneSizeEpithelialCell" in data and "bareNuclei" in data and "chromatin" in data and "normalNucleoli" in data and "mitosis" in data:
        sample_code = data["sampleCodeNumber"]

        # Business Logic
        result = pred.predict_sample(data["agglomerateThickness"], 
                                                    data["cellSizeUniformity"], 
                                                    data["cellShapeUniformity"], 
                                                    data["marginalAdherence"], 
                                                    data["oneSizeEpithelialCell"], 
                                                    data["bareNuclei"], 
                                                    data["chromatin"], 
                                                    data["normalNucleoli"], 
                                                    data["mitosis"])

        # API Response
        return {
            'sampleCode': sample_code,
            'hitPercentage': 95,
            'result': result,
        }
    else:
        return {'error': 'Campos inválidos no JSON recebido'}


if __name__=='__main__':
    app.run()
