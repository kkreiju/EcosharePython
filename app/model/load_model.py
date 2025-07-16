import tensorflow as tf # type: ignore
import os

MODEL_PATH = os.getenv("MODEL_PATH", "model_files/cnn_model.h5")

def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

# Global model load for reuse
model = load_model()
