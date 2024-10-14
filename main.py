from fastapi import FastAPI, Depends, HTTPException
from auth import verify_token, create_token  # Importe a função de criação de token
from scraping import load_csv_from_url, load_local_csv
import os
import logging

logging.basicConfig(level=logging.INFO)


app = FastAPI(
   title="Embrapa CSV API",
   description="API para consulta de dados CSV da Embrapa",
   version="1.0.0"
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

@app.post("/token", tags=["Authentication"])
def generate_token():
    """
    Endpoint para gerar o token JWT.
    """
    try:
        token = create_token({"user": "embrapa_user"})
        logging.info(f"Token gerado: {token}")
        return {"token": token}
    except Exception as e:
        logging.error(f"Erro ao gerar token: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")



@app.get("/csv_data/", tags=["CSV Data"])
def get_all_csv_data(token: dict = Depends(verify_token)):
   """
   Retorna os dados de todos os CSVs a partir das URLs.
   """
   all_data = {}
   for key, url in CSV_URLS.items():
       try:
           df = load_csv_from_url(url)
           all_data[f"arquivo_{key}"] = df.to_dict(orient='records')
       except ValueError as e:
           all_data[f"arquivo_{key}"] = {"error": str(e)}
   return all_data


@app.get("/csv_data/{file_id}", tags=["CSV Data"])
def get_csv_by_id(file_id: int, token: dict = Depends(verify_token)):
   """

   Retorna os dados de um CSV específico identificado por file_id.
   """
   url = CSV_URLS.get(file_id)
   if url:
       try:
           df = load_csv_from_url(url)
           if df is None or df.empty:
               raise HTTPException(status_code=404, detail="Dados do CSV estão vazios")
           return df.to_dict(orient='records')
       except ValueError as e:
           raise HTTPException(status_code=400, detail=str(e))
   else:
        raise HTTPException(status_code=404, detail="CSV não encontrado")