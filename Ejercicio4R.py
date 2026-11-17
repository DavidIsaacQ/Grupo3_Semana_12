#Ejercicio 4 - Contador de vocales

def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    contador = 0

    for letra in texto.lower():
        if letra in vocales:
            contador += 1

    return contador


palabra = input("Ingrese un texto: ")
print(f"En el texto hay {contar_vocales(palabra)} vocales")

