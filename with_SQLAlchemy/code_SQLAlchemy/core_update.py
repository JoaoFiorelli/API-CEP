from sqlalchemy import update
from core_test import endereco_table, engine

conn = engine.connect()

up = update(endereco_table).where(endereco_table.c.CEP == '23654896')

up = up.values(CEP=14052390)

result = conn.execute(up)

print(result.rowcount)