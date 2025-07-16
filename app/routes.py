from flask import Blueprint, request, jsonify # type: ignore
from .model.predict import predict_class
from .model.predict import predict_top3

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    result = predict_top3(image)
    return jsonify(result)

# Sample curl command to test the /predict endpoint
# curl -X POST -F "image=@C:/Users/beesquit/Desktop/testcolor.png" http://localhost:5000/predict

# Add /test endpoint
@api.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'hello world'})
