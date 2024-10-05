#Se obtiene la cantidad de estudiantes, verificando que se un dígito/valor numerico o que sea mayor a 0
def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    numero = input("¿Cuántos estudiantes tiene?: ")
    while not numero.isdigit() or int(numero) <= 0:
        print("Por favor, introduzca un valor válido. Debe ser número y positivo")
        numero = input("Ingrese cantidad total de estudiantes: ")
    print("--------------------\n\n")
    return int(numero) 

def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    nombre = input("Ingrese el nombre del estudiante: ")
    print("--------------------")
    return nombre

def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    cant_asignaturas = input("Ingrese el n° de asignaturas: ")
    while not cant_asignaturas.isdigit() or int(cant_asignaturas) <= 0:
        print("Por favor, introduzca un valor válido. Debe ser número positivo.")
        cant_asignaturas = input("Ingrese el n° de asignaturas: ")
    return int(cant_asignaturas) 

def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    calificaciones = {}
    for i in range(num_asignaturas):
        nombre_asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ")
        calificacion = input(f"Ingrese la calificación de la asignatura {nombre_asignatura}: ")
        while not calificacion.isdigit() or float(calificacion) <= 0 or float(calificacion) > 10:
            print("Por favor, introduzca un valor válido. Debe ser número positivo entre 0 y 10.")
            calificacion = input(f"Ingrese la calificación de la asignatura {nombre_asignatura}: ")
        calificaciones[nombre_asignatura] = float(calificacion)
    print("--------------------")
    return calificaciones

def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    return (sum(calificaciones.values()) / len(calificaciones))

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    if promedio >= 6.0:
        return "Aprobado"
    else:
        return "Reprobado"

def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    print("\n\nResumen de los estudiantes:")
    print("---------------------------")
    for i in estudiantes:
        print(f"Nombre: {i['nombre']}")
        print(f"Promedio: {i['promedio']}")
        print(f"Estado: {i['estado']}")
        print("\n---------------------------\n")


num_estudiantes = obtener_numero_estudiantes()
estudiantes = []

for _ in range(num_estudiantes):
    nombre = obtener_nombre_estudiante()
    num_asignaturas = obtener_numero_asignaturas()
    calificaciones = obtener_calificaciones(num_asignaturas)
    promedio = calcular_promedio(calificaciones)
    estado = determinar_estado(promedio)
    
    estudiantes.append({
        'nombre': nombre,
        'promedio': promedio,
        'estado': estado
    })

imprimir_resumen(estudiantes)