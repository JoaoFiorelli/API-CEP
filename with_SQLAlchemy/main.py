from fastapi import FastAPI
from Database import buscaCEP

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
        return {"Erro": "Digite um CEP válido"}

    else:

        endereco = buscaCEP.list_endereco()

        for end in endereco:
                        
            if end[1] == cep_id:                
                return {"CEP": end["CEP"], "Endereço": end["Rua"], "Numero": end["Numero"], 
                        "Complemento": end["Complemento"]}
            
        return {"Erro": "CEP não enconrado"}      

@app.get("/cep/{cep_id}")
def str_or_not(cep_id):

    if type(cep_id) == str:
        if cep_id.isnumeric() == True:
            return read_cep(int(cep_id))
        else:
            return {"Erro": "Entre com um valor numérico"}

    if type(cep_id) == int:
        return read_cep(cep_id)

