from sqlalchemy import select
from core import endereco_table, engine

def list_endereco():

    conn = engine.connect()

    sel = select(endereco_table)
    result = list(conn.execute(sel))

    return result

# endereco = list_endereco()
# for end in endereco:
#     print(end)
#     print(end["CEP"])