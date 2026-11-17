
from fastapi import FastAPI, APIRouter
from app.routers import projects, evaluations


app = FastAPI(title = "Mini Evaluacion Expo IBERO")

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(router=projects.router)
api_v1.include_router(router=evaluations.router)

app.include_router(router=api_v1)

@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo desde FASTAPI :)"}


# def buscar_proyecto(proyecto_id: int) -> Proyecto:
#     proyecto = repositorio.obtener_proyecto(proyecto_id)
#     if proyecto is None:
#         raise HTTPException(status_code = 404, detail = "Proyecto no encontrado")
#     return proyecto
    

# @app.get("/")
# def raiz():
#     return {"mensaje" : "Hola mundo desde FastAPI!"}

# @app.post("/proyectos", response_model=Proyecto, status_code=201)
# def crear_proyecto(datos: ProyectoIn):
#     return repositorio.crear_proyecto(datos)

# @app.get("/proyectos", response_model=list[Proyecto])
# def listar_proyectos(
#     categoria: Categoria | None = None,
#     limite: Annotated[int, Query(ge=1, le=100)] = 10, 
# ):
#     return repositorio.listar_proyectos(categoria, limite)

# @app.get("/proyetos/{proyecto_id}", response_model=Proyecto)
# def obtener_proyecto(proyecto_id: int):
#     return buscar_proyecto(proyecto_id)

# @app.get("/proyetos/{proyecto_id}/evaluaciones", response_model=Evaluacion, status_code = 201)
# def crear_evaluacion(proyecto_id: int, datos: EvaluacionIn):
#     buscar_proyecto(proyecto_id)
#     return repositorio.crear_evaluacion(proyecto_id, datos)

# @app.get("/proyetos/{proyecto_id}/evaluaciones", response_model= list[Evaluacion])
# def listar_evaluaciones(proyecto_id: int):
#     buscar_proyecto(proyecto_id)
#     return repositorio.crear_evaluacion(proyecto_id)

# @app.get("/proyectos/{proyecto_id}/resumen", response_model = Resumen)
# def resumen_proyecto(proyecto_id: int):
#     buscar_proyecto(proyecto_id)
#     return repositorio.resumen(proyecto_id)