import tkinter as tk
import conexaoAPI
# Criando a janela principal
def interface():
    janela = tk.Tk()
    janela.title("Chagas Clima Tempo")
    janela.geometry("700x700")  # Largura x Altura
    # Adicionando um rótulo
    rotulo = tk.Label(janela, text="Quer saber a Temperatura de qual lugar?", font=("Arial", 21))
    rotulo.pack(pady=100)  # Espaçamento vertical
    # entrada de dados via texto
    entrada_cidade = tk.Entry(janela)
    entrada_cidade.pack()
    
    #exibição de resultado
    rotulo_resultado = tk.Label(janela, text="", font=("Arial",16))
    rotulo_resultado.pack(pady=27)
    # Iniciando o loop da interface
    
    def buscandoClima():
        APIKEY = "cacb868c5f1a95eedfa7ed3bda5773ea"
        cidade = entrada_cidade.get()
        if not cidade:
            rotulo_resultado.config(text="Escreva uma cidade")
        URL = conexaoAPI.criacaoAPI(cidade, APIKEY)
        if conexaoAPI.identificacao_erro(URL) == False:
            rotulo_resultado.config(text="Erro, cidade não existente")
        temperatura, pais, clima = conexaoAPI.informacoesGeraisCidades(URL)
        rotulo_resultado.config(text=f"A temperatura em {cidade} é {temperatura} graus celcius\n Localizado no país {pais}\n No geral, condições climaticas: {clima}")
    # botão buscar
    botao_buscar = tk.Button(janela, text="Buscar Clima", command=buscandoClima)
    botao_buscar.pack()
    janela.mainloop()
        
interface()