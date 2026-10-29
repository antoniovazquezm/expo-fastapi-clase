from enum import Enum #enum valida y selecciona una lista
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from app.schemas import Categoria, Proyecto, ProyectoIn


app = FastAPI(title = "Mini Evaluacion Expo IBERO")



#TODO: Camibar despues a SQLModel
proyectos: dict[int, Proyecto] = {}
siguiente_id = 1

    

@app.get("/")
def raiz():
    return {"mensaje" : "Hola mundo desde FastAPI!"}

@app.post("/proyectos", response_model=Proyecto, status_code=201)
def crear_proyecto(datos: ProyectoIn):
    global siguiente_id
    proyecto = Proyecto(id=siguiente_id, **datos.model_dump()) #** funciona como un apuntador a lo que está detrás del contenido
    proyectos[proyecto.id] = proyecto
    siguiente_id +=1
    return proyecto

@app.get("/proyectos", response_model=list[Proyecto])
def listar_proyectos(
    categoria: Categoria | None = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 10, 
):
    resultado = [
        p for p in proyectos.values()
        if categoria is None or p.categoria == categoria
    ]
    return resultado [:limite]

@app.get("/proyetos/{proyecto_id}", response_model=Proyecto)
def obtener_proyecto(proyecto_id: int):
    if proyecto_id not in proyectos:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyectos[proyecto_id]