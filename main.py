import json 
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/cep/{cep_id}")
def read_item(cep_id: int):

    with open('myfile.json') as f:
        endereco = json.load(f) 
    endereco = dict(endereco) 

    for end in endereco.values():
        for key, item in end.items():
                
            if item == cep_id:   
             
                return {"CEP": item, "Endereço": end["Rua"], "Numero": end["Numero"], 
                        "Complemento": end["Complemento"]}
            
    return {"CEP não enconrado": cep_id}
      