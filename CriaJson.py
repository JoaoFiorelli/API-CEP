import json

"""
MODELO
data = {
    "CEP": cep_id
    "Rua": rua_id
    "Numero": num_id
    "Complemento": complem_id
}
"""

data = {
    "endereco 1": {
        "CEP": 17245452,
        "Rua": "Governador Lopes",
        "Numero": 235,
        "Complemento": "ap 56"
    },
    "endereco 2": {
        "CEP": 95325754,
        "Rua": "Maria do ceu",
        "Numero": 689,
        "Complemento": "ap 23"
    },
    "endereco 3": {
        "CEP": 36245965,
        "Rua": "Machado de assis",
        "Numero": 364,
        "Complemento": 0        
    },
}

out_file = open("myfile.json", "w")
json.dump(data, out_file)
out_file.close()

with open('myfile.json') as f:
      endereco = json.load(f)
      print(endereco)
