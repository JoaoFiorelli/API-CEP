from core import endereco_table, engine

conn = engine.connect()

ins = endereco_table.insert()

# new_endereco = ins.values(CEP=17512420,
#                           Rua='Rua Machado de Assis',
#                           Numero=326,
#                           Complemento='Apto. 46')

# conn.execute(new_endereco)

conn.execute(endereco_table.insert(), [
    {
        "CEP": 17245452,
        "Rua": "Governador Lopes",
        "Numero": 235,
        "Complemento": "ap 56"
    },
    {
        "CEP": 95325754,
        "Rua": "Maria do ceu",
        "Numero": 689,
        "Complemento": "ap 23"
    },
    {
        "CEP": 36245965,
        "Rua": "Machado de assis",
        "Numero": 364,
        "Complemento": "Terreo"        
    },
    {
        "CEP": 23654896,
        "Rua": "Drummond",
        "Numero": 44,
        "Complemento": "Apto. 8"        
    },
    {
        "CEP": 56534256,
        "Rua": "Inacio da Silva",
        "Numero": 4,
        "Complemento": ""        
    },
    {
        "CEP": 96328752,
        "Rua": "Quinze de Abril",
        "Numero": 89,
        "Complemento": "Esquina"       
    }
])