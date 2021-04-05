from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/cep/{cep_id}")
def read_item(cep_id: int):
    return {"CEP": cep_id}
      