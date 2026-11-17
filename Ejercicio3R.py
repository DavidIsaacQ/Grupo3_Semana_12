# Ejercicio 3 - Clasificador de temperatura

def clasificar_temperatura(temp):
    if temp <10:
        return "Frío"
    elif temp <20:
        return "Fresco"
    elif temp <30:
        return "Calido"
    else:
        return "Caliente"

temperatura = int(input("Ingrese la temperatura: "))
print(f"La temperatura es {clasificar_temperatura(temperatura)}")
