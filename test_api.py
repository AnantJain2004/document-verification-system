import requests

url = "http://127.0.0.1:5000/predict"

files = {"file": open("temp/test2.pdf", "rb")}

response = requests.post(url, files=files)

print(response.json())