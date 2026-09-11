from eii_utils import limpiar_consola
hay_trato_iphone:bool = True
nota1:int = 80
nota2:int = 86
nota3:int = 75
nota4:int = 80
auto_abuela:int = 6
auto_mama:int = 6

hay_trato_iphone = ( (nota1+nota2+nota3+nota4)/4 >= 80 and nota1 >= 75 and nota2 >= 75 and nota3 >= 75 and nota4 >= 75 ) \
    and (auto_abuela >= 8 or auto_mama >= 8 or (auto_mama+auto_abuela) >= 12)

limpiar_consola()
print(f"Hay trato para el Iphone {hay_trato_iphone}")