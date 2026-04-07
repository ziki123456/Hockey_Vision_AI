# app.py
# Flask aplikace pro HockeyVision.
# Nejdriv urci hokej / neni_hokej.
# Kdyz je to hokej, pak urci situaci.

import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from predict import load_trained_models, predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

binary_model = None
situation_model = None
models_loaded = False

try:
    print("Nacitam modely...")
    binary_model, situation_model = load_trained_models()
    models_loaded = True
    print("Modely jsou nactene.")
except Exception as e:
    print(f"Modely zatim nejsou pripravene: {e}")


def allowed_file(filename):
    if "." not in filename:
        return False
    extension = filename.rsplit(".", 1)[1].lower()
    return extension in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html", models_loaded=models_loaded)


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "Nebyl odeslan zadny obrazek."}), 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return jsonify({"error": "Nebyl vybran zadny soubor."}), 400

    if not allowed_file(image_file.filename):
        return jsonify({"error": "Nepovoleny typ souboru. Pouzij png jpg jpeg nebo webp."}), 400

    try:
        safe_name = secure_filename(image_file.filename)
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], safe_name)
        image_file.save(save_path)

        if not models_loaded or binary_model is None or situation_model is None:
            return jsonify({
                "final_class_name": "MODELY_ZATIM_NEJSOU_VLOZENE",
                "binary_class_name": "-",
                "binary_confidence_percent": 0,
                "binary_raw_output": 0,
                "situation_class_name": None,
                "situation_confidence_percent": None,
                "saved_file": safe_name
            })

        result = predict_image(
            save_path,
            binary_model=binary_model,
            situation_model=situation_model
        )

        response = {
            "final_class_name": result["final_class_name"],
            "binary_class_name": result["binary_class_name"],
            "binary_confidence_percent": round(result["binary_confidence"] * 100, 2),
            "binary_raw_output": round(result["binary_raw_output"], 4),
            "situation_class_name": result["situation_class_name"],
            "situation_confidence_percent": (
                round(result["situation_confidence"] * 100, 2)
                if result["situation_confidence"] is not None else None
            ),
            "saved_file": safe_name
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"Nastala chyba pri predikci: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)