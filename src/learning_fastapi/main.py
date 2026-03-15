from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {"id": 1, "title": "Primer Post", "content": "Este es el primer post"},
    {"id": 2, "title": "Segundo Post", "content": "Este es el segundo post"},
]

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Bienvenido a mi API</h1>"

@app.get("/posts")
def get_posts():
    return posts

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"message": f"¡Hola, {nombre}!"}
