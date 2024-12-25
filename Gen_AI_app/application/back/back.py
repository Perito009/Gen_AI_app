# application/back/back.py

from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle pickle
with open('../model/avocado_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
