from eii_utils import limpiar_consola
esta_soleado:bool = True
presupuesto:int = 100_000
es_fin_mes:bool = True
tareas_pendiente:int=0
# en esta también podría ser solo una variable bool que diga si hay pendientes o no
pelicula:str = "El Coyote vrs ACME"
tenemos_cupones_mama_maria:bool=True
entradas_papa_carlos:bool=True

salimos_fin_semana = (esta_soleado and presupuesto >= 100_000 and es_fin_mes) or \
    (presupuesto >= 10_000 and tareas_pendiente == 0) or \
    (pelicula == "El Coyote vrs ACME" and (tenemos_cupones_mama_maria or entradas_papa_carlos))

limpiar_consola()
print(f"Planificación del fin de semana {salimos_fin_semana}")