import requests

APIKEY = "cacb868c5f1a95eedfa7ed3bda5773ea"

def criacaoAPI(cidade, APIKEY):
    URL = "https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=" + APIKEY
    return URL
def identificacao_erro(URL):
    resposta = requests.get(URL)
    if resposta.status_code == 200:
        return True
    elif resposta.status_code == 404:
        return False
    else:
        return False
def informacoesGeraisCidades(URL):
    todasInformacoes = requests.get(URL)
    informacoesCidades = todasInformacoes.json()
    temperatura = round((informacoesCidades["main"]["temp"])-273.15)
    pais = informacoesCidades["sys"]["country"]
    clima = informacoesCidades["weather"][0]["description"]
    return temperatura, pais, clima
# def exibicao(temperatura, cidade, pais, clima):
#     print(f"A temperatura em {cidade} é {temperatura} graus celcius\n Localizado no país {pais}\n no geral condições climaticas: {clima}")
# # como encadear essa funções? Função Main
# def main():
#     cidade = input(f"Digite o nome da cidade que quer Consultar:\n ")
#     URL = criacaoAPI(cidade, APIKEY)
#     if identificacao_erro(URL) == True:
#        temperatura, clima, pais = informacoesGeraisCidades(URL)
#     elif identificacao_erro(URL) == False:
#         erro = "Erro 404"
#         print(f"Erro {erro} certifique-se de que a cidade existe")
#     return exibicao(temperatura, cidade, pais, clima)
# main()
        