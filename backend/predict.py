import numpy as np
import joblib

# Carregar o modelo
model = joblib.load('breast_cancer_model.h5')

def predict_sample(thickness, size_uniformity, shape_uniformity, adhesion, epithelial_size,
                   bare_nuclei, chromatin, nucleoli, mitoses):
    sample = np.array([[thickness, size_uniformity, shape_uniformity, adhesion, epithelial_size,
                        bare_nuclei, chromatin, nucleoli, mitoses]])
    predicted_class = model.predict(sample)[0]

    if predicted_class == 2:
        result = 'BENIGNO'
    else:
        result = 'MALIGNO'

    return result