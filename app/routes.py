from flask import Blueprint, request, jsonify
from .model.predict import predict_class

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    result = predict_class(image)
    return jsonify(result)

# Add /test endpoint
@api.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'hello world'})
