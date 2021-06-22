from sqlalchemy import select
from core import endereco_table

sel = select([endereco_table])

for row in sel.execute():
    print(row)