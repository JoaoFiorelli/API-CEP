import json 
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/cep/{cep_id}")
def read_item(cep_id: int):

    with open('myfile.json') as f:
        endereco = json.load(f) 
    endereco = dict(endereco) 

    if endereco["endereco 3"["CEP"]] == cep_id:       
        return {"CEP buscado": cep_id, "Endereco encontrado": endereco["endereco 3"]}
    else:
        return "CEP não enconrado"
      