from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float
    taxa: float | None = None

app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    return item

# ===== Corpo da requisição + parâmetros de rota + parâmetros de consulta =====
# curl -X PUT "http://127.0.0.1:8000/items/42?q=promocao" \
#   -H "Content-Type: application/json" \
#   -d '{"nome": "Teclado", "preco": 150.0}'

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# Os parâmetros da função serão reconhecidos conforme abaixo:
# Se o parâmetro também é declarado no path, será utilizado como um parâmetro de rota.
# Se o parâmetro é de um tipo único (como int, float, str, bool, etc) será interpretado como um parâmetro de consulta.
# Se o parâmetro é declarado como um modelo Pydantic, será interpretado como o corpo da requisição.

# Como o FastAPI identifica cada parâmetro nesta rota:
# - item_id (Path | Obrigatório): está declarado na rota {item_id} e precisa ser um int (/items/42).
# - item (Body/JSON | Obrigatório): por ser um modelo Pydantic (Item), é lido automaticamente do corpo da requisição.
# - q (Query | Opcional): tipo simples (str) que não está na rota e tem valor padrão None (?q=...).