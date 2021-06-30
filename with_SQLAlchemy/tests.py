from starlette.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("cep,resultado", [
    ("36245965", {"CEP":36245965,"Endereço":"Machado de assis","Numero":364,"Complemento":"Terreo"}),
    ("3624454574", {"Erro": "Digite um CEP válido"}),
    ("string", {"Erro": "Entre com um valor numérico"}),
    ("14211947", {"Erro": "CEP não enconrado"})
])
def test_main_response_json(cep, resultado):
    endpoint = f"/cep/{cep}"

    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json() == resultado
   