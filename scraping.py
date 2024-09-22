import requests
import pandas as pd
from io import StringIO

def load_csv_from_url(url: str, delimiter=';', header=0):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        csv_data = StringIO(response.text)
        try:
            df = pd.read_csv(csv_data, delimiter=delimiter, header=header)
            df.fillna('None', inplace=True)  # ou outro método apropriado
            return df
        except pd.errors.ParserError as e:
            raise ValueError(f"Erro ao processar o CSV: {e}")
    else:
        raise ValueError(f"Erro ao baixar o CSV. Status code: {response.status_code}")

def load_local_csv(file_path: str, delimiter=';', header=0):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter, header=header)
        return df
    except pd.errors.ParserError as e:
        raise ValueError(f"Erro ao processar o CSV: {e}")
