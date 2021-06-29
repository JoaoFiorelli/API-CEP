from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String)

engine = create_engine('sqlite:///enderecos.db',
                        echo=True)

metadata = MetaData(bind=engine)

endereco_table = Table('endereco', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('CEP', Integer, index=True),
                        Column('Rua', String(100)),
                        Column('Numero', Integer),
                        Column('Complemento', String(40)))

metadata.create_all()