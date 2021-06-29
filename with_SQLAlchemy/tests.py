from starlette.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get("/cep/{cep_id}")

    assert response.status_code == 200

def test_main_response_string():
    response = client.get("/cep/string")

    assert response.json() == {"Erro": "Entre com um valor numérico"}

@pytest.mark.parametrize("cep,resultado", [
    ("36245965", {"CEP":36245965,"Endereço":"Machado de assis","Numero":364,"Complemento":"Terreo"}),
    ("3624454574", {"Erro": "Digite um CEP válido"})
])
def test_main_response_json(cep, resultado):
    endpoint = f"/cep/{cep}"

    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json() == resultado
   