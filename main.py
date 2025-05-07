from estudiantes.registro import cargar_estudiantes, ordenar_y_mostrar_estudiantes, calcular_promedio

def main():
    # Ruta del archivo CSV
    ruta = "estudiantes/estudiantes.csv"
    
    # Cargar estudiantes desde el archivo
    estudiantes = cargar_estudiantes(ruta)
    
    # Verificar si hay estudiantes válidos
    if not estudiantes:
        print("No se encontraron estudiantes válidos.")
        return
    
    # Mostrar la lista de estudiantes ordenados
    print("\nLista de estudiantes:")
    ordenar_y_mostrar_estudiantes(estudiantes)
    
    # Calcular y mostrar el promedio de las notas
    print("\nPromedio de notas:")
    calcular_promedio(estudiantes)

if __name__ == "__main__":
    main()