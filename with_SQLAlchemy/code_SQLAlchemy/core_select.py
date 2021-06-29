from sqlalchemy import select
from core_test import endereco_table

sel = select([endereco_table])
sel.execute()

for row in sel.execute():
    print(row)