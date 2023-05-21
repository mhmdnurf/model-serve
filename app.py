import requests

# Google Cloud Run
# resp = requests.post("https://prediksi-fli6ldqjaa-et.a.run.app/", files={'file': open('./sample/five.png', 'rb')})

# Localhost with flask
# resp = requests.post("http://127.0.0.1:5000", files={'file': open('./sample/five.png', 'rb')})

# Localhost with FastAPI
resp = requests.post("http://localhost:8000", files={'file': open('./sample/three.png', 'rb')})

print(resp.json())
	