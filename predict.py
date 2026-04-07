# predict.py
# Nacteni 2 modelu a predikce:
# 1) hokej / neni_hokej
# 2) pokud je hokej urceni situace

import os
import numpy as np
from PIL import Image
import tensorflow as tf

BINARY_IMAGE_SIZE = (224, 224)
SITUATION_IMAGE_SIZE = (224, 224)

BINARY_MODEL_PATH = os.path.join("model", "binary_hockey_model.keras")
SITUATION_MODEL_PATH = os.path.join("model", "hockey_situations_model.keras")

BINARY_CLASS_NAMES = {
    0: "HOKEJ",
    1: "NENI_HOKEJ"
}

SITUATION_CLASS_NAMES = [
    "JIZDA_S_PUKEM",
    "KLIDOVA_SITUACE",
    "SOUBOJ_U_MANTINELU",
    "VHAZOVANI",
    "ZAKROK_BRANKARE"
]


def load_model_file(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model nebyl nalezen: {model_path}")
    return tf.keras.models.load_model(model_path)


def load_trained_models():
    binary_model = load_model_file(BINARY_MODEL_PATH)
    situation_model = load_model_file(SITUATION_MODEL_PATH)
    return binary_model, situation_model


def preprocess_image(image_source, target_size=(224, 224)):
    img = Image.open(image_source).convert("RGB")
    img = img.resize(target_size)

    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def predict_binary_image(image_source, model):
    prepared_image = preprocess_image(image_source, target_size=BINARY_IMAGE_SIZE)

    raw_output = float(model.predict(prepared_image, verbose=0)[0][0])

    predicted_class_index = 1 if raw_output > 0.5 else 0
    predicted_class_name = BINARY_CLASS_NAMES[predicted_class_index]

    if predicted_class_index == 1:
        confidence = raw_output
    else:
        confidence = 1 - raw_output

    return {
        "predicted_class_index": predicted_class_index,
        "predicted_class_name": predicted_class_name,
        "probability_raw": raw_output,
        "confidence": float(confidence)
    }


def predict_situation_image(image_source, model):
    prepared_image = preprocess_image(image_source, target_size=SITUATION_IMAGE_SIZE)

    raw_output = model.predict(prepared_image, verbose=0)[0]
    predicted_class_index = int(np.argmax(raw_output))
    predicted_class_name = SITUATION_CLASS_NAMES[predicted_class_index]
    confidence = float(raw_output[predicted_class_index])

    return {
        "predicted_class_index": predicted_class_index,
        "predicted_class_name": predicted_class_name,
        "probabilities": raw_output.tolist(),
        "confidence": confidence
    }


def predict_image(image_source, binary_model=None, situation_model=None):
    if binary_model is None or situation_model is None:
        binary_model, situation_model = load_trained_models()

    binary_result = predict_binary_image(image_source, binary_model)

    final_result = {
        "binary_class_name": binary_result["predicted_class_name"],
        "binary_confidence": binary_result["confidence"],
        "binary_raw_output": binary_result["probability_raw"],
        "final_class_name": binary_result["predicted_class_name"],
        "situation_class_name": None,
        "situation_confidence": None
    }

    if binary_result["predicted_class_name"] == "HOKEJ":
        situation_result = predict_situation_image(image_source, situation_model)

        final_result["final_class_name"] = situation_result["predicted_class_name"]
        final_result["situation_class_name"] = situation_result["predicted_class_name"]
        final_result["situation_confidence"] = situation_result["confidence"]

    return final_result


if __name__ == "__main__":
    test_image_path = input("Zadej cestu k obrazku: ").strip()

    try:
        binary_model, situation_model = load_trained_models()

        result = predict_image(
            test_image_path,
            binary_model=binary_model,
            situation_model=situation_model
        )

        print("\nVYSLEDEK PREDIKCE")
        print("-----------------")
        print(f"Binarni vysledek: {result['binary_class_name']}")
        print(f"Binarni jistota: {result['binary_confidence'] * 100:.2f} %")

        if result["situation_class_name"] is not None:
            print(f"Situace: {result['situation_class_name']}")
            print(f"Jistota situace: {result['situation_confidence'] * 100:.2f} %")
        else:
            print("Situace se neurcovala protoze obrazek neni hokej.")

    except Exception as e:
        print(f"Nastala chyba: {e}")