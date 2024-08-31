'''
Crear una lista con 10 números enteros, recorrerla haciendo uso de la 
sentencia for, e imprimir en pantalla el valor de cada elemento indicando
si es par, impar o cero.
'''
lista = [0, 25, 48, 100, 39, 94, 68, 87, 55, 18] # indices de número <=100
for i in lista:
    if i == 0:
        print (f"{i} es cero")
    elif i % 2 == 0:
        print (f"{i} es par")
    else:
        print (f"{i} es impar")