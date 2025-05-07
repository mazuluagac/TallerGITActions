from estudiantes.registro import cargar_estudiantes, ordenar_y_mostrar_estudiantes, calcular_promedio

def main():
    ruta = "estudiantes/estudiantes.csv"
    estudiantes = cargar_estudiantes(ruta)
    
    if not estudiantes:
        print("No se encontraron estudiantes válidos.")
        return
    
    print("\nLista de estudiantes:")
    ordenar_y_mostrar_estudiantes(estudiantes)
    
    #print("\nCálculo del promedio:")
    print("\nPromedio de notas:")
    calcular_promedio(estudiantes)

if __name__ == "__main__":
    main()
    input("\nPresiona Enter para salir...")