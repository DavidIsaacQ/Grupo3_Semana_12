# Ejercicio 6 - Clase producto con descuento

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def vender(self, cant):
        if cant <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cant > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cant
        return self.precio * cant

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: S/. {self.precio} | Stock: {self.stock} unidades"


laptop = Producto("Laptop", 2500, 5)
print(laptop)

laptop.aplicar_descuento(10)
print("Con descuento: ", laptop)

total_venta = laptop.vender(2)
print(f"Total vendido: S/ {total_venta}")
print("Despues de venta", laptop)

try:
    laptop.vender(10)
except ValueError as e:
    print("Error", e)
    