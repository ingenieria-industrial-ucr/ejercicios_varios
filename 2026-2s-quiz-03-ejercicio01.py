from eii_utils import (
    limpiar_consola,
    leer_flotante_opcional,
    leer_booleano_opcional,
    leer_entero_opcional,
    imprimir_mensaje,
    imprimir_advertencia,
    imprimir_error,
)

titulo: str = ""
# Variables #1
cumple_requerimientos_tecnicos: bool = True
temperatura: float = 180
es_presion_optima: bool = True
cumple_requerimientos_insumos: bool = True
hay_materia_prima_disponible: bool = True
hay_orden_reabastecimiento: bool = True
# Variables #2
operarios_capacitados: int = 3
es_turno_nocturno: bool = True
# Variables #3
esta_aprobada_inspeccion: bool = True
hay_mantenimiento_pendiente: bool = True

limpiar_consola()
# Entradas 01
titulo = "Requerimientos técnicos"
print(f"{titulo.upper():^40}")
temperatura = leer_flotante_opcional("Digite la temperatura", temperatura)
es_presion_optima = leer_booleano_opcional(
    "La presión está en un nivel óptimo", es_presion_optima
)
print()
titulo = "Requerimientos de insumos"
print(f"{titulo.upper():^40}")
hay_materia_prima_disponible = leer_booleano_opcional(
    "Hay materia prima disponible", hay_materia_prima_disponible
)
hay_orden_reabastecimiento = leer_booleano_opcional(
    "Hay orden reabastecimiento", hay_orden_reabastecimiento
)

# Procesamiento #1
cumple_requerimientos_tecnicos = temperatura >= 180 and es_presion_optima
cumple_requerimientos_insumos = (
    hay_materia_prima_disponible or hay_orden_reabastecimiento
)

limpiar_consola()
if cumple_requerimientos_tecnicos and cumple_requerimientos_insumos:
    titulo = "Lote autorizado"
    print(f"{titulo.upper():^40}")
    operarios_capacitados = leer_entero_opcional(
        "Cantidad de operararios", operarios_capacitados
    )
    es_turno_nocturno = leer_booleano_opcional(
        "La planta está en turno nocturno", es_turno_nocturno
    )
    if operarios_capacitados >= 3 and es_turno_nocturno:
        imprimir_mensaje("Línea 1 (Alta Velocidad)")
    else:
        imprimir_advertencia("Línea 2 (Estándar/Supervisada)")
else:
    titulo = "Lote no autorizado"
    print(f"{titulo.upper():^40}")
    esta_aprobada_inspeccion: bool = leer_booleano_opcional(
        "Esta aprobada la inspección de calidad", esta_aprobada_inspeccion
    )
    hay_mantenimiento_pendiente: bool = leer_booleano_opcional(
        "Hay mantenimiento pendiente", hay_mantenimiento_pendiente
    )
    if esta_aprobada_inspeccion and hay_mantenimiento_pendiente:
        imprimir_error("Paro Técnico Obligatorio")
    else:
        imprimir_error("Detenido en Espera de Materia Prima")
