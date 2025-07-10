from .load_model import model
from .utils import preprocess_image

# Example class names (update based on your training)
CLASS_NAMES = ['Blue', 'Red', 'Yellow', 'Other']

def predict_class(image_file):
    processed_image = preprocess_image(image_file)
    predictions = model.predict(processed_image)
    predicted_index = predictions.argmax()
    confidence = float(predictions[0][predicted_index])

    if confidence < 0.6:
        return {'prediction': 'Other', 'confidence': round(confidence * 100, 2)}

    return {
        'prediction': CLASS_NAMES[predicted_index],
        'confidence': round(confidence * 100, 2)
    }
