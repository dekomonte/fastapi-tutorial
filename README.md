# fastapi-tutorial
Tutorial FastAPI Docs.

[Tutorial - Guia de Usuário](https://fastapi.tiangolo.com/pt/tutorial/)

---
## Anotações

#### Modelos Pydantic
[**Pydantic**](https://pydantic.dev/docs/) é uma biblioteca Python para executar a validação de dados. 

#### Schema
* Um "schema" é uma definição ou descrição de algo. Não o código que o implementa, mas apenas uma descrição abstrata. 
* O termo "schema" também pode se referir à forma de alguns dados, como um conteúdo JSON. Nesse caso, significaria os atributos JSON e os tipos de dados que eles possuem, etc.

#### Métodos HTTP
Ao construir APIs, você normalmente usa esses métodos HTTP para executar uma ação específica.

Normalmente você usa:

* POST: para criar dados.
* GET: para ler dados.
* PUT: para atualizar dados.
* DELETE: para deletar dados.

---
## Links
[Installing uv](https://docs.astral.sh/uv/getting-started/installation/) </br>
[Pydantic Validation](https://pydantic.dev/docs/validation/latest/get-started/) </br>
[FastAPI Cloud](https://fastapicloud.com/) </br>
[The OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification)
[JSON Schema](https://json-schema.org/)

---

# Como executar

`uv run fastapi dev`
```
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/openapi.json
```

#### entrypoint configurado
`fastapi dev` ou `fastapi run`