# Calculadora basica

def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b != 0:
            return a / b
        else:
            print("Error, no se puede dividir por cero")
            

    else:
        print("Operador no valido")
        


x = float(input("Ingrese un número: "))
y = float(input("Ingrese el segundo número: "))
z = input("Ingrese un operador ( + - * / ): ")

print(f"El resultado es {calcular(x, y, z):.2f}")