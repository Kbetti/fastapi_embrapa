from fastapi.testclient import TestClient
from main import app  # Certifique-se de que o app está sendo importado corretamente
from auth import create_token  # Importe a função para criar o token

client = TestClient(app)

# Gera um token válido antes de cada teste
def get_valid_token():
    payload = {"sub": "test_user"}  # Altere conforme sua necessidade
    return create_token(payload)

# Testando o endpoint root
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API para consulta de dados CSV da Embrapa"}

# Testando o endpoint que retorna todos os CSVs
def test_get_all_csv_data():
    token = get_valid_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/csv_data/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    # Checar se os arquivos CSV estão presentes
    for i in range(1, 6):
        assert f"arquivo_{i}" in response.json()

# Testando o endpoint que retorna um CSV específico
def test_get_csv_by_id():
    token = get_valid_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/csv_data/1', headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deveria retornar uma lista de registros


