import matematicas_utiles as mu


def reporte_geometrico(radios):
    # Encabezado de la tabla con alineación de columnas
    print(f"{'Radio':<10} | {'Área':<12} | {'Perímetro':<12}")
    print("-" * 38)

    for r in radios:
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)
        print(f"{r:<10.2f} | {area:<12.2f} | {perimetro:<12.2f}")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    lista_radios = [1, 2.5, 5, 10]
    reporte_geometrico(lista_radios)
