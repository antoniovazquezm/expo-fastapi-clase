from app.schemas import Categoria, Proyecto, ProyectoIn

class RepositoryMemory:
    def __init__(self) -> None:
        self.proyectos : dict[int, Proyectos] = {}
        self.evaluaciones : dict[int, Evaluacion] = {}
        self.siguiente_id = 1
        self.siguiente_evaluacion_id = 1

    #Proyectos
    def crear_proyecto(self, datos: ProyectoIn) -> Proyecto:
        proyecto = Proyecto(id = self.siguiente_id, **datos.model_dump())
        self.proyectos[proyecto.id] = proyecto
        self.siguiente_id += 1
        return proyecto

    def listar_proyecto(self, categoria: Categoria | None, limite: int) -> list[Proyecto]:
        resutlado = [
            p for p in proyectos.values()
            if categoria is None or p.categoria == categoria
        ]
        return resultado [:limite]

    def obtener_proyecto(self, proyecto_id : int) -> Proyecto | None:
        return self.proyectos.get(proyecto_id)

    #Evaluaciones

    def crear_evaluacion(self, proyecto_id : int, datos: EvaluacionIn) -> Evaluacion:
        evaluacion = Evaluacion(
            id = self.siguiente_evaluacion_id,
            proyecto_id = proyecto_id,
            **datos.model_dump())
        self.evaluaciones[evaluacion.id] = evaluacion
        self.siguiente_evaluacion_id += 1
        return evaluacion

    def listar_evaluaciones(self, proyecto_id : int) -> list[Evaluacion] :
        return [e for e in self.evaluaciones.values() if e.proyecto_id == proyecto_id]
    
    def resumen(self, proyecto_id: int) -> Resumen:
        del_proyecto = [e for e in self.evaluaciones.values() if e.proyecto_id == proyecto_id]
        total = len(del_proyecto)
        if total == 0:
            return Resumen (
                proyecto_id = proyecto_id, total_evaluaciones=0,
                innovacion = None, viabilidad = None, presentacion = None, general = None,
            )
        innovacion = sum(e.innovacion for e in del_proyecto) / total
        viabilidad = sum(e.viabilidad for e in del_proyecto) / total
        presentacion = sum(e.presentacion for e in del_proyecto) / total
        general = (innovacion + viabilidad + presentacion) / 3
        return Resumen(
            proyecto_id = proyecto_id,
            total_evaluaciones = total,
            innovacion = round(innovacion, 2),
            viabilidad = round(viabilidad, 2),
            presentacion = round(presentacion, 2),
            general = round(general, 2)
        )

repositorio = RepositoryMeory()


