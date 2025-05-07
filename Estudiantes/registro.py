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

def mostrar_estudiantes_tabla(estudiantes):
    """
    Muestra los estudiantes ordenados alfabéticamente en formato tabular.
    """
    if not estudiantes:
        print("No hay estudiantes válidos para mostrar.")
        return

    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[0])
    print(f"{'Nombre':<20} {'Nota':>5}")
    print("-" * 26)
    for nombre, nota in estudiantes_ordenados:
        print(f"{nombre:<20} {nota:>5.2f}")
