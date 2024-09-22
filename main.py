from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import verify_token
from scraping import load_csv_from_url, load_local_csv
import os

app = FastAPI(
    title="Embrapa CSV API",
    description="API para consulta de dados CSV da Embrapa",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URLs dos CSVs
CSV_URLS = {
    1: "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    2: "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    3: "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    4: "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    5: "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
}

# Endpoints

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "API para consulta de dados CSV da Embrapa"}

@app.get("/csv_data/", tags=["CSV Data"])
def get_all_csv_data(token: dict = Depends(verify_token)):
    all_data = {}
    dataframes = {}  # Dicionário para armazenar DataFrames individuais
    for key, url in CSV_URLS.items():
        try:
            df = load_csv_from_url(url)
            all_data[f"arquivo_{key}"] = df.to_dict(orient='records')
            dataframes[key] = df  # Armazena o DataFrame no dicionário
        except Exception as e:
            all_data[f"arquivo_{key}"] = {"error": str(e)}

    # Agora você pode usar `dataframes` para acessar cada DataFrame separadamente
    # Exemplo de uso:
    # df_1 = dataframes[1]

    return all_data

@app.get("/csv_data/{file_id}", tags=["CSV Data"])
def get_csv_by_id(file_id: int, token: dict = Depends(verify_token)):
    url = CSV_URLS.get(file_id)
    if url:
        try:
            print(f"Tentando carregar CSV da URL: {url}")  # Log da URL
            df = load_csv_from_url(url)
            if df is None or df.empty:
                raise HTTPException(status_code=404, detail="Dados do CSV estão vazios")
            return df.to_dict(orient='records')
        except ValueError as e:
            print(f"Erro ao carregar CSV: {str(e)}")  # Log do erro
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="CSV não encontrado")

