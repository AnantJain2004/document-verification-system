import requests

url = "https://doc-verifier.onrender.com/predict"

files = {"file": open("test.pdf", "rb")}

response = requests.post(url, files=files)

print(response.json())