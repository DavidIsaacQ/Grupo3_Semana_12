class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        if not (0 <= porcentaje <= 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self.precio -= self.precio * (porcentaje / 100)

    def vender(self, cant):
        if cant <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a 0.")
        if cant > self.stock:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}")
        self.stock -= cant
        return self.precio * cant

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} unidades"


if __name__ == "__main__":
    laptop = Producto("Laptop Gamer", 1200.0, 5)
    print(laptop)

    laptop.aplicar_descuento(15)
    print("Con descuento ->", laptop)

    total = laptop.vender(2)
    print(f"Venta realizada por ${total:.2f} ->", laptop)

    try:
        laptop.vender(10)
    except ValueError as e:
        print("Error capturado:", e)
