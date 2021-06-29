from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get("/cep/{cep_id}")
    assert response.status_code == 200

def test_main_response_string():
    response = client.get("/cep/string")
    assert response.json() == {"Erro": "Entre com um valor numérico"}

def test_main_response_dig_mais():
    response = client.get("/cep/123456789")
    assert response.json() == {"Erro": "Digite um CEP válido"}

def test_main_response_json():
    response = client.get("/cep/36245965")
    assert response.status_code == 200
    assert response.json() == {"CEP":36245965,"Endereço":"Machado de assis","Numero":364,"Complemento":"Terreo"}