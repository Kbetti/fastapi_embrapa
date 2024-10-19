from fastapi import FastAPI, Depends, HTTPException
from auth.auth import verify_token, create_token  # Importe a função de criação de token
from loader.loader import load_csv_from_url
import logging


logging.basicConfig(level=logging.INFO)


app = FastAPI(
   title="Embrapa CSV API",
   description="API para consulta de dados CSV da Embrapa",
   version="1.0.0"
)

# URLs dos CSVs
CSV_URLS = {
   'producao': "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
   'processa': "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
   'comercio': "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
   'importacao': "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
   'exportacao': "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
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



@app.get("/{file_id}", tags=["CSV Data"])
def get_csv_by_id(file_id: str, token: dict = Depends(verify_token)):
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