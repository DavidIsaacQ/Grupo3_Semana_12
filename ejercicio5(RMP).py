import csv

estudiantes = []

with open("estudiantes.csv", mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)

  for fila in lector:
    nombre = fila["nombre"]
    notas = [
        float(valor) for clave, valor in fila.items() if clave != "nombre"
    ]

    promedio = sum(notas) / len(notas)
    estudiantes.append({"nombre": nombre, "promedio": promedio})

print("--- Promedio por alumno ---")
for est in estudiantes:
  print(f"{est['nombre']}: {est['promedio']:.2f}")

top_alumno = max(estudiantes, key=lambda x: x["promedio"])
print(
    f"\nTop alumno: {top_alumno['nombre']} con promedio de"
    f" {top_alumno['promedio']:.2f}"
)

aprobados = sum(1 for est in estudiantes if est["promedio"] >= 13)
print(f"Total de aprobados (prom >= 13): {aprobados}")
