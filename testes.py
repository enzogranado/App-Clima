import requests
APIKEY = "cacb868c5f1a95eedfa7ed3bda5773ea"
cidade = "santo andre"
URL = "https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=" + APIKEY
resposta = requests.get(URL)
print(resposta.status_code)
print(resposta.json())
informacoesCidades = resposta.json()
clima = informacoesCidades['weather'][0]['description']
print(clima)