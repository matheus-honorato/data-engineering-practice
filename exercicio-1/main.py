import os
import requests
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]
pasta_destino = "downloads/"

def main():
    for i in range(len(download_uris)):
        response = requests.get(download_uris[i])
        if response.ok:
            os.makedirs(pasta_destino, exist_ok=True)    
            file_name = os.path.join(pasta_destino, download_uris[i].split("/")[-1])
            with open(file_name, mode = "wb") as f:
                f.write(response.content)    
            with zipfile.ZipFile(file_name, mode= "r") as zip_file:
                zip_file.extractall(pasta_destino)
            os.remove(file_name)
            print("baixado com sucesso", file_name)
        else:
            print("Erro ao baixar", file_name.split("/")[-1])



if __name__ == "__main__":
    main()
