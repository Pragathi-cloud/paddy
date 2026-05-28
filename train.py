import requests

url = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.tflite"

response = requests.get(url)

with open("yolov8n.tflite", "wb") as f:
    f.write(response.content)

print("Downloaded successfully!")
