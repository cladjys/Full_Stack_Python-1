# Dada una lista de diccionarios que representan información de estudiantes, 
# realiza las siguientes tareas:

estudiantes = [
    {"nombre":"Juan", "edad": 17, "calificaciones": [85, 90, 88]},
    {"nombre":"María", "edad": 19, "calificaciones": [92, 89, 90]},
    {"nombre":"Pedro", "edad": 21, "calificaciones": [85, 95, 80]},
    {"nombre":"Ana", "edad": 18, "calificaciones": [90, 92, 87]},
    {"nombre":"Luis", "edad": 20, "calificaciones": [88, 85, 92]},
    ]

# Deinir la función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
# Filtra y muestra únicamente los estudiantes que tienen más de 18 años 
# y cuyo promedio de calificaciones sea superior a 85.'''

estudiantes_filtrados = []
for estudiante in estudiantes:
    # calcular promedio de las calificaciones
    promedio_notas = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
    #filtrar estudiante
    if estudiante["edad"] > 18 and promedio_notas > 85:
        estudiantes_filtrados.append(estudiante)
    # Imprimir el filtro
        print (estudiante)

#Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años 
# y cuya edad sea un número primo.

promedio_primos = []
for estudiante in estudiantes:

    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        promedio_primos.extend(estudiante['calificaciones'])
        
# Promedio de calificaciones de estudiantes con edad primo
promedio_calificaciones = sum(promedio_primos) / len(promedio_primos) if promedio_primos else 0

print (promedio_calificaciones)
