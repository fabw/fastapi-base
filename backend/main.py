from fastapi import FastAPI
from db import conectar_db
from llamar_api import buscar_noticias



app = FastAPI()





@app.get("/listo")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}


@app.get("/buscar_noticias")
def obtener_noticias():
    query = "chile"

    noticias = buscar_noticias(query)


    return {
        "noticias":noticias
    }