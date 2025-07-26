import tensorflow as tf # type: ignore

PLANT_MODEL_PATH = "model_files/plant_model.keras"
LISTING_MODEL_PATH = "model_files/listing_model.keras"

def load_plant_model():
    model = tf.keras.models.load_model(PLANT_MODEL_PATH)
    return model

def load_listing_model():
    model = tf.keras.models.load_model(LISTING_MODEL_PATH)
    return model

# Global model load for reuse
plant_model = load_plant_model()
listing_model = load_listing_model()