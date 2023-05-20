import requests

resp = requests.post("https://prediksi-fli6ldqjaa-et.a.run.app/", files={'file': open('six.png', 'rb')})

print(resp.json())
	