import tensorflow as tf # type: ignore

MODEL_PATH = "model_files/plant_model.keras"

def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

# Global model load for reuse
model = load_model()
