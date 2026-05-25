import requests
from utils.ocr import extract_text

file_path = "test.pdf"
text = extract_text(file_path)

print(text[:500])
url = "https://doc-verifier.onrender.com/predict"

files = {"file": open("temp/test.pdf", "rb")}

response = requests.post(url, files=files)

print("JSON:",response.json())