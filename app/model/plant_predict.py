from .load_model import load_plant_model
from .utils import preprocess_base64_image

# Class names for plant health classification
CLASS_NAMES = [
    'Bell Pepper Healthy', 'Bell Pepper Unhealthy',
    'Bitter Gourd Healthy', 'Bitter Gourd Unhealthy',
    'Cabbage Healthy', 'Cabbage Unhealthy',
    'Carrots Healthy', 'Carrots Unhealthy',
    'Chayote Healthy', 'Chayote Unhealthy',
    'Eggplant Healthy', 'Eggplant Unhealthy',
    'Spinach Healthy', 'Spinach Unhealthy',
    'Squash Healthy', 'Squash Unhealthy',
    'Tomato Healthy', 'Tomato Unhealthy'
]

def predict_class(image_file):
    model = load_plant_model()  # Lazy load the model
    processed_image = preprocess_base64_image(image_file)
    predictions = model.predict(processed_image)
    predicted_index = predictions.argmax()
    confidence = float(predictions[0][predicted_index])

    return {
        'prediction': CLASS_NAMES[predicted_index],
        'confidence': round(confidence * 100, 2)
    }

def predict_top3(base64_image):
    """Get top 3 predictions from base64 image"""
    model = load_plant_model()  # Lazy load the model
    processed_image = preprocess_base64_image(base64_image)
    predictions = model.predict(processed_image)[0]
    top3_indices = predictions.argsort()[-3:][::-1]
    results = []
    for idx in top3_indices:
        results.append({
            'class': CLASS_NAMES[idx],
            'confidence': round(float(predictions[idx]) * 100, 2)
        })
    return {'top3': results}
