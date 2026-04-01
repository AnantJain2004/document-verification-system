# 📄 Document Verification System (PYQ & Notes Classifier)

## 🚀 Overview

This project is a **Document Verification System** designed for university students to upload and validate study materials such as:

* Previous Year Question Papers (PYQs)
* Notes (printed or scanned)

The system automatically checks whether the uploaded document is **valid academic content** or **irrelevant/malicious content**.

---

## 🧠 Features

* ✅ Supports **text-based PDFs**
* ✅ Supports **scanned PDFs (image-based)**
* ⚠️ Partial support for **handwritten notes**
* ✅ OCR-based text extraction
* ✅ Machine Learning classification
* ✅ Rule-based filtering for better accuracy
* ✅ REST API for integration with frontend/backend

---

## ⚙️ Tech Stack

* Python
* Flask (API)
* Scikit-learn (ML Model)
* Tesseract OCR (Text extraction)
* pdf2image (PDF → Images)
* Docker (Containerization)

---

## 🔄 System Workflow

1. User uploads PDF
2. PDF is converted into images
3. OCR extracts text from images
4. Text is cleaned and preprocessed
5. Rule-based filtering is applied
6. ML model classifies the document
7. Result returned: **Valid / Invalid**

---

## 📁 Project Structure

```
project/
│
├── app.py
├── test_api.py
├── requirements.txt
├── Dockerfile
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── training/
│   ├── train.py
│   └── dataset.csv
│
├── utils/
│   ├── ocr.py
│   ├── preprocess.py
│   └── rules.py
```

---

## 🛠️ Setup Instructions (Without Docker)

### 1. Install Python (3.8+)

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install OCR & PDF Tools

* Install **Tesseract OCR**
[Download](https://github.com/UB-Mannheim/tesseract/wiki)
* Install **Poppler**
[Download](https://github.com/oschwartz10612/poppler-windows/releases/tag/v25.12.0-0)

### 4. Update paths in `utils/ocr.py` (if needed)

---

## ▶️ Run the Project

### Step 1: Train Model

```
python training/train.py
```

### Step 2: Start API

```
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing the API

### Option 1: Using Postman

* Method: POST
* URL:

```
http://127.0.0.1:5000/predict
```

* Body → form-data:

  * Key: `file`
  * Type: File
  * Upload PDF

---

### Option 2: Using Python

```
python test_api.py
```

---

## 🐳 Docker Setup (Recommended)

### 1. Build Docker Image

```
docker build -t doc-verifier .
```

### 2. Run Container

```
docker run -p 5000:5000 doc-verifier
```

---

## 📤 API Endpoint

### POST `/predict`

**Request:**

* Form-data with key `file` (PDF)

**Response:**

```
{
  "result": "Valid Study Material"
}
```

---

## ⚠️ Limitations

* Handwritten notes may not be fully accurate
* OCR may produce noisy text for low-quality scans
* Model accuracy depends on dataset quality

---

## 🎯 Future Improvements

* Improve handwritten text recognition
* Integrate with frontend UI
* Deploy on cloud

---

## 📌 Conclusion

This project demonstrates a practical implementation of **OCR + Machine Learning + Rule-Based Systems** to solve a real-world problem faced by students.

---

⭐ Feel free to contribute or suggest improvements!
