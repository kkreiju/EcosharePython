import tensorflow as tf # type: ignore
import os

# Configure TensorFlow for better memory management
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Reduce TensorFlow logging
tf.config.experimental.enable_memory_growth = True

# Configure GPU memory growth if available
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(f"GPU configuration error: {e}")

PLANT_MODEL_PATH = "model_files/plant_model.keras"
LISTING_MODEL_PATH = "model_files/listing_model.keras"

# Global variables for lazy loading
_plant_model = None
_listing_model = None

def load_plant_model():
    global _plant_model
    if _plant_model is None:
        print("🔄 Loading plant model...")
        _plant_model = tf.keras.models.load_model(PLANT_MODEL_PATH)
        print("✅ Plant model loaded successfully")
    return _plant_model

def load_listing_model():
    global _listing_model
    if _listing_model is None:
        print("🔄 Loading listing model...")
        _listing_model = tf.keras.models.load_model(LISTING_MODEL_PATH)
        print("✅ Listing model loaded successfully")
    return _listing_model

# Lazy loading - models loaded only when first accessed
@property
def plant_model():
    return load_plant_model()

@property  
def listing_model():
    return load_listing_model()