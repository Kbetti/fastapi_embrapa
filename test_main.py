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


# Testando o endpoint que retorna um CSV específico
def test_get_csv_by_id():
    token = get_valid_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/exportacao', headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deveria retornar uma lista de registros


