import json 
from fastapi import FastAPI

app = FastAPI()

def validation_len(cep_id):

    if len(str(cep_id)) == 8:
        status_val = 1
        return status_val 
    else:
        status_val = 0
        return status_val

def read_cep(cep_id):

    status = validation_len(cep_id)  

    if status == 0: 

        return "Digite um CEP válido"

    else:

        with open('myfile.json') as f:
            endereco = json.load(f) 
        endereco = dict(endereco) 

        for end in endereco.values():
                        
            if end["CEP"] == cep_id:   
             
                return {"CEP": end["CEP"], "Endereço": end["Rua"], "Numero": end["Numero"], 
                        "Complemento": end["Complemento"]}
            
        return "CEP não enconrado"      

@app.get("/cep/{cep_id}")
def str_or_not(cep_id):

    if type(cep_id) == str:
        if cep_id.isnumeric() == True:
            return read_cep(int(cep_id))
        else:
            return "Entre com um valor numérico"

    if type(cep_id) == int:
        return read_cep(cep_id)

