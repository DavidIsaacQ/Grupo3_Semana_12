def contar_vocales (texto):
    contador = 0
    for vocales in texto:
        if vocales.lower() in "aeiouáéíóú":
            contador += 1
    return contador

print (contar_vocales ("Menos miedo, Más vida"))