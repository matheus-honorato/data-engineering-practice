## Exercícios práticos de engenharia de dados
O objetivo deste repositório é desenvolver e aprender habilidades importantes para o dia a dia de um engenheiro de dados, solucionando uma lista de problemas práticos como:

  - Processamento de dados em Python
  - Manipulação de arquivos CSV, simples, parquet, JSON, etc.
  - Design de tabelas de banco de dados SQL
  - Uso de Python com PostgreSQL para ingestão e recuperação de dados
  - Utilização de PySpark
  - Limpeza de dados sujos

#### Exercício 1 - Baixando arquivos
Neste exercício, foi realizada a implementação de um código em Python capaz de:

  - Baixar uma lista de arquivos zip
  - Criar um diretório chamado "downloads"
  - Extrair cada arquivo CSV do zip
  - Excluir cada arquivo zip
  - Salvar os arquivos CSV extraídos na pasta "downloads"
  - Renomear os arquivos

Repositório: [Exercício 1](https://github.com/matheus-honorato/data-engineering-practice/tree/main/exercicio-1)


#### Exercício 2 - Web Scraping + Download + Pandas
Neste exercício, eu precisei fazer o download de um arquivo da [página](https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/), pra isso precisei:
  - Realizar um web scraping da página
  - Encontrar o arquivo correspondente a `2024-01-19 10:16` e  ao tamanho `128K`
  - Construir a `url` necessária para o download
  - Criar um diretório chamado `downloads` e gravar o arquivo no diretório
  - Realizar a leitura do arquivo csv baixado utilizando `pandas`
  - Encontrar o registro com maior temperatura `HourlyDryBulbTemperature` e imprimir sua saída
  - Por fim, excluir o arquivo csv baixado.

Repositório: [Exercício 2](https://github.com/matheus-honorato/data-engineering-practice/tree/main/exercicio-2)
