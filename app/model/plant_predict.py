from .load_model import plant_model
from .utils import preprocess_image

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
    processed_image = preprocess_image(image_file)
    predictions = plant_model.predict(processed_image)
    predicted_index = predictions.argmax()
    confidence = float(predictions[0][predicted_index])

    if confidence < 0.6:
        return {'prediction': 'Other', 'confidence': round(confidence * 100, 2)}

    return {
        'prediction': CLASS_NAMES[predicted_index],
        'confidence': round(confidence * 100, 2)
    }


# New function: get top 3 predictions
def predict_top3(image_file):
    processed_image = preprocess_image(image_file)
    predictions = plant_model.predict(processed_image)[0]
    top3_indices = predictions.argsort()[-3:][::-1]
    results = []
    for idx in top3_indices:
        results.append({
            'class': CLASS_NAMES[idx],
            'confidence': round(float(predictions[idx]) * 100, 2)
        })
    return {'top3': results}
