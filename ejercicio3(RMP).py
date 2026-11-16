def clasificar_temperatura(temp):
    if temp < 10:
        return "Frio"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Calido"
    else: 
        return "Caliente"

print (clasificar_temperatura(30))