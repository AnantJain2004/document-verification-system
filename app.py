from flask import Flask, request, jsonify
import pickle
from utils.ocr import extract_text
from utils.preprocess import clean_text
from utils.rules import rule_check

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    file_path = "temp.pdf"
    file.save(file_path)

    # Step 1: OCR
    text = extract_text(file_path)

    if len(text.strip()) < 30:
        return jsonify({"result": "Low readable content (possibly handwritten)"})

    # Step 2: Clean
    text = clean_text(text)

    # Step 3: Rule
    rule = rule_check(text)

    # Step 4: ML
    vec = vectorizer.transform([text])
    ml = model.predict(vec)[0]

    # Final decision
    if rule or ml == 1:
        result = "Valid Study Material"
    else:
        result = "Invalid Document"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)