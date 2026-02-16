from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI funciona!"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"message": f"¡Hola, {nombre}!"}
