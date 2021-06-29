from sqlalchemy import delete
from core_test import endereco_table, engine

conn = engine.connect()

dell = delete(endereco_table).where(endereco_table.c.CEP == 17512420)

result = conn.execute(dell)

print(result.rowcount)