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
kWh: float = 0
cargo_por_energia: float = 0
sub_total: float = 0
total: float = 0
alumbrado_publico: float = 0
impuesto_bomberos: float = 0
iva: float = 0

limpiar_consola()
titulo = "Calculo de factura de energía"
print(f"{titulo.upper():^40}")
kWh = leer_entero_opcional("Digite su consumo de kWh al mes",30)

if kWh <= 30:
    cargo_por_energia = 1744.80
elif kWh <= 200:
    cargo_por_energia = 1744.80 + (kWh - 30) * 58.16
elif kWh <= 200:
    cargo_por_energia = 1744.80 + 58.16 * 170 + (kWh - 200) * 89.24
else:
    cargo_por_energia = 1744.80 + 58.16 * 170 + 89.24 * 100 + (kWh - 300) * 92.27




alumbrado_publico = 3.02 * kWh

if kWh <= 100:
    impuesto_bomberos = 0
elif kWh <= 1750:
    impuesto_bomberos = cargo_por_energia * 1.75 /100
else:
    impuesto_bomberos = 154200.10 * 1.75 /100

sub_total = cargo_por_energia + alumbrado_publico + impuesto_bomberos

if kWh <= 280:
    iva = 0
else:
    iva = (sub_total-1744.80) * 0.13

total = sub_total + iva


reporte = f"""
==================================================
        DESGLOSE DE FACTURA ELÉCTRICA (CNFL)
==================================================
Consumo mensual:{kWh:26,.2f} kWh
--------------------------------------------------
Subtotal Energía:              ₡{cargo_por_energia:14,.2f}
Alumbrado Público:             ₡{alumbrado_publico:14,.2f}
Tributo a Bomberos (1.75%):    ₡{impuesto_bomberos:14,.2f}
Impuesto IVA (13%):            ₡{iva:14,.2f}
--------------------------------------------------
TOTAL A PAGAR:                 ₡{total:14,.2f}
==================================================
"""

print(reporte)