from flask import Flask, request, jsonify
import pickle
import os
from utils.ocr import extract_text
from utils.preprocess import clean_text
from utils.rules import rule_check

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "Document Verification API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify(False), 400

        file = request.files["file"]
        file_path = "temp.pdf"
        file.save(file_path)

        # Step 1: OCR
        text = extract_text(file_path)

        if len(text.strip()) < 30:
            os.remove(file_path)
            print("Low readable content")
            return jsonify(False)

        # Step 2: Clean
        text = clean_text(text)

        # Step 3: Rule
        rule = rule_check(text)

        # Step 4: ML
        vec = vectorizer.transform([text])
        ml = model.predict(vec)[0]

        # Final decision
        if rule or ml == 1:
            return jsonify(True)
        else:
            return jsonify(False)

    except Exception as e:
        print("Error:", str(e))
        return jsonify(False)
    
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)