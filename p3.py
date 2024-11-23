print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def longitud(obj):
    contador = 0
    for elemento in obj:
        contador += 1
    return contador

#Usa la función con una lista
lista = [1, 2, 3, 4, 5]
print(longitud(lista)) #Imprime 5

#Usa la función con una cadena
cadena = "Hola, mundo!"
print(longitud(cadena)) #Imprime 13
