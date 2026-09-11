from eii_utils import limpiar_consola

premio_por_esfuezo:bool = True

nota1:int = 80
nota2:int = 86
nota3:int = 75
nota4:int = 80
auto_papa:int = 6
auto_mama:int = 6

premio_por_esfuezo = ( (nota1+nota2+nota3+nota4)/4 >= 75 and nota1 >= 70 and nota2 >= 70 and nota3 >= 70 and nota4 >= 75 ) \
    and (auto_papa >= 6 or auto_mama >= 10 or (auto_mama+auto_papa) >= 14)

limpiar_consola()
print(f"El premio por esfuerzo {premio_por_esfuezo}")