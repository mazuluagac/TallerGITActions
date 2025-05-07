from estudiantes.registro import cargar_estudiantes, ordenar_y_mostrar_estudiantes

def main():
    ruta = "estudiantes/estudiantes.csv"
    estudiantes = cargar_estudiantes(ruta)
    
    if not estudiantes:
        print("No se encontraron estudiantes válidos.")
        return
    
    print("\n Lista de estudiantes:")
    ordenar_y_mostrar_estudiantes(estudiantes)

if __name__ == "__main__":
    main()
    input("\nPresiona Enter para salir...")
