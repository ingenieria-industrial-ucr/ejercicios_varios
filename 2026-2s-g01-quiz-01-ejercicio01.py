from eii_utils import limpiar_consola

vamos_salir:bool=True

esta_soleado:bool = True
presupuesto:int = 95_000
es_sabado:bool = True
tareas_pendientes:int = 0 # también podría ser una variable booleana
pelicula:str = "El Coyote vrs ACME"
tenemos_cupones_mama_maria:bool=True
entradas_papa_carlos:bool=True

vamos_salir = (esta_soleado and presupuesto >= 95_000 and es_sabado) or \
    (presupuesto >= 15_000 and tareas_pendientes == 0) or \
    (pelicula == "El Coyote vrs ACME" and (tenemos_cupones_mama_maria or entradas_papa_carlos))

limpiar_consola()
print(f"¿vamos a salir? {vamos_salir}")