import requests

resp = requests.post("https://prediksi-fli6ldqjaa-et.a.run.app/", files={'file': open('./sample/five.png', 'rb')})

print(resp.json())
	