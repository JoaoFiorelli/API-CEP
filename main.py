import json 
from fastapi import FastAPI

app = FastAPI()


@app.get("/cep/{cep_id}")
def read_cep(cep_id: int):

    with open('myfile.json') as f:
        endereco = json.load(f) 
    endereco = dict(endereco) 

    for end in endereco.values():
                        
        if end["CEP"] == cep_id:   
             
            return {"CEP": end["CEP"], "Endereço": end["Rua"], "Numero": end["Numero"], 
                    "Complemento": end["Complemento"]}
            
    return "CEP não enconrado"      