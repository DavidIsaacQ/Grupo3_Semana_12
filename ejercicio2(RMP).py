def calcular(N1, N2, Operador):

    if Operador == "+":
        return N1 + N2
    elif Operador == "-":
        return N1 - N2
    elif Operador == "*":
        return N1 * N2
    elif Operador == "/":
        if N2 != 0:
            return N1 / N2
        else:
            print (f"Error: No es posible dividir entre cero")
            return None
    
print (calcular(5,4, "+"))
print (calcular(6,3, "-"))
print (calcular(3,4, "*"))
print (calcular(3,0, "/"))
