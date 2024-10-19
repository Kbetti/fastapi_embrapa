import requests
import pandas as pd
from io import StringIO

def load_csv_from_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status 4xx/5xx
        
        # Usa o Pandas para ler o conteúdo CSV
        from io import StringIO
        csv_data = StringIO(response.text)  # Converte o texto da resposta em um objeto semelhante a arquivo
        df = pd.read_csv(csv_data)  # Lê o CSV para um DataFrame
        return df
    except Exception as e:
        print(f"Erro ao carregar CSV da URL: {e}")
        return None

def load_local_csv(file_path: str, delimiter=';', header=0):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter, header=header)
        return df
    except pd.errors.ParserError as e:
        raise ValueError(f"Erro ao processar o CSV: {e}")
