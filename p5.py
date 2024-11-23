print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def sum_lista(lista):
    #Inicializamos la variable de suma en 0
    suma = 0
    #Recorremos todos los elementos de la lista y los sumamos
    for numero in lista:
        suma += numero
    return suma

def multip_lista(lista):
    #Inicializamos la variable de producto en 1
    producto = 1
    #Recorremos todos los elementos de la lista y los multiplicamos
    for numero in lista:
        producto *= numero
    return producto

print(sum_lista([1, 2, 3, 4]))  #Debería devolver 10
print(multip_lista([1, 2, 3, 4]))  #Debería devolver 24
