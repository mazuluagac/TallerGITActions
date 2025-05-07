from estudiantes.registro import cargar_estudiantes

def main():
    ruta = "estudiantes/estudiantes.csv"
    estudiantes = cargar_estudiantes(ruta)
    
    if not estudiantes:
        print("No se encontraron estudiantes válidos.")
        return
    
    print("\n Lista de estudiantes:")
    for nombre, nota in estudiantes:
        print(f"{nombre:10} - {nota:.2f}")

if __name__ == "__main__":
    main()
    input("\nPresiona Enter para salir...")
