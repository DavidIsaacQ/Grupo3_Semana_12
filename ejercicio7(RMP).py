celsius = [0, 10, 20, 30, 37, 100]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

productos = [
    {"nombre": "Teclado", "precio": 45},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Mouse", "precio": 20},
]
ordenados_por_precio = sorted(productos, key=lambda item: item["precio"])
print("Ordenados por precio:", ordenados_por_precio)
