from fastapi import APIRouter, Query, status

from app.dependencies import buscar_proyecto
from app.repository import repositorio
from app.schemas import Evaluacion, EvaluacionIn, Resumen

router = APIRouter(prefix= "/proyectos/{proyecto_id}/evaluaciones", tags=["Evaluaciones"])

@router.get("/proyetos/{proyecto_id}/evaluaciones", response_model=Evaluacion, status_code = 201)
def crear_evaluacion(proyecto_id: int, datos: EvaluacionIn):
    buscar_proyecto(proyecto_id)
    return repositorio.crear_evaluacion(proyecto_id, datos)

@router.get("/proyetos/{proyecto_id}/evaluaciones", response_model= list[Evaluacion])
def listar_evaluaciones(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.crear_evaluacion(proyecto_id)

@router.get("/proyectos/{proyecto_id}/resumen", response_model = Resumen)
def resumen_proyecto(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.resumen(proyecto_id)