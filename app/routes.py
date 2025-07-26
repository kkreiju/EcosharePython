from flask import Blueprint, request, jsonify # type: ignore
from .model.plant_predict import predict_class as plant_predict_class
from .model.listing_predict import predict_class as listing_predict_class
from .model.plant_predict import predict_top3 as plant_predict_top3
from .model.listing_predict import predict_top3 as listing_predict_top3

api = Blueprint('api', __name__)

@api.route('/api/plant', methods=['POST'])
def predict_plant():
    try:
        # Only accept JSON requests with base64 image
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        if 'image' not in request.json:
            return jsonify({'error': 'Missing "image" key in JSON'}), 400
        
        base64_image = request.json['image']
        if not base64_image:
            return jsonify({'error': 'Empty base64 image data'}), 400
        
        result = plant_predict_class(base64_image)
        return jsonify(result)
            
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

@api.route('/api/listing', methods=['POST'])
def predict_listing():
    try:
        # Only accept JSON requests with base64 image
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        if 'image' not in request.json:
            return jsonify({'error': 'Missing "image" key in JSON'}), 400
        
        base64_image = request.json['image']
        if not base64_image:
            return jsonify({'error': 'Empty base64 image data'}), 400

        result = listing_predict_class(base64_image)
        return jsonify(result)
            
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

@api.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'OK'}), 200
