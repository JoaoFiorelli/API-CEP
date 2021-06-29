from sqlalchemy import select
from Database import core
#from core import endereco_table, engine

def list_endereco():

    conn = core.engine.connect()

    sel = select(core.endereco_table)
    result = list(conn.execute(sel))

    return result

# endereco = list_endereco()
# for end in endereco:
#     print(end)
#     print(end["CEP"])