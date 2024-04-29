import requests
import pandas as pd
import os
from bs4 import BeautifulSoup



def main():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    headers = {"User-Agent" : user_agent}
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    response = requests.get(url, headers=headers)
    data_buscada = "2024-01-19 10:16"
    size_busca = "128K" #limitando a quantidade de arquivos
    
    url_download = []
    pasta_destino = "downloads/"

    existe_arquivo = False #Verificar se o arquivo foi baixado
    if (response.ok):

        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        resultado = soup.find_all("tr")
        for linha in resultado:
            coluna=linha.find_all("td")
            if(len(coluna)>2):
                data = coluna[1].get_text().strip()
                size = coluna[2].get_text().strip()
                if(data == data_buscada.strip()):
                    if(size == size_busca.strip()):
                        link = coluna[0].find("a")
                        if link:
                            url_download.append(url+link.get("href"))
        os.makedirs(pasta_destino, exist_ok=True) ##Criando a pasta downloads
        caminho_arquivo = os.path.join(pasta_destino,url_download[0].split("/")[-1])
        arquivo = requests.get(url_download[0])
        if arquivo.ok:
            with open(caminho_arquivo, mode="wb") as f:
                f.write(arquivo.content)
                existe_arquivo = True
        
    else:
        print("Solicitação falhou. Código do status:", response.status_code)


    if(existe_arquivo):
        df = pd.read_csv(caminho_arquivo)
        temp_max_index = df['HourlyDryBulbTemperature'].idxmax()
        temp_max = df['HourlyDryBulbTemperature'][temp_max_index]
        print(temp_max)
        os.remove(caminho_arquivo)
    else:
        "Arquivo não existe"



    

    


if __name__ == "__main__":
    main()
