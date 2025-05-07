import csv

def cargar_estudiantes(ruta_csv):
    """
    Carga estudiantes desde un archivo CSV, validando que las notas estén entre 0.0 y 5.0.
    Devuelve una lista de tuplas (nombre, nota).
    """
    estudiantes = []
    try:
        with open(ruta_csv, mode='r', encoding='utf-8', newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    nota = float(fila["nota"])
                    if 0.0 <= nota <= 5.0:
                        estudiantes.append((fila["nombre"], nota))
                except (ValueError, KeyError):
                    continue
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_csv}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return estudiantes

def ordenar_y_mostrar_estudiantes(estudiantes):
    """
    Ordena a los estudiantes alfabéticamente y los imprime en formato tabular.
    """
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return

    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[0])
    print(f"{'Nombre':<20} {'Nota':>5}")
    print("-" * 26)
    for nombre, nota in estudiantes_ordenados:
        print(f"{nombre:<20} {nota:>5.2f}")       

def calcular_promedio(estudiantes):
    """
    Calcula el promedio de las notas de los estudiantes y lo muestra con dos decimales.
    """
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio.")
        return

    promedio = sum(nota for _, nota in estudiantes) / len(estudiantes)
    print(f"El promedio general de las notas es: {promedio:.2f}")