import numpy as np # type: ignore
from PIL import Image # type: ignore
import base64
import io

def preprocess_base64_image(base64_string, target_size=(224, 224)):
    """
    Convert base64 encoded image string to preprocessed numpy array
    """
    try:
        # Remove data URL prefix if present (e.g., "data:image/jpeg;base64,")
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # Decode base64 string
        image_bytes = base64.b64decode(base64_string)
        
        # Convert to PIL Image
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image = image.resize(target_size)
        image_array = np.array(image) / 255.0  # Normalize
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
        return image_array
    except Exception as e:
        raise ValueError(f"Error processing base64 image: {str(e)}")
