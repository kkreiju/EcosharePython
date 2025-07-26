from flask import Blueprint, request, jsonify # type: ignore
from .model.plant_predict import predict_top3 as plant_predict_top3
from .model.listing_predict import predict_top3 as listing_predict_top3

api = Blueprint('api', __name__)

@api.route('/api/plant', methods=['POST'])
def predict_plant():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    result = plant_predict_top3(image)
    return jsonify(result)

@api.route('/api/listing', methods=['POST'])
def predict_listing():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    result = listing_predict_top3(image)
    return jsonify(result)
