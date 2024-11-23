print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def es_vocal(caracter):
    #Convertir el carácter a minúsculas para no diferenciar entre mayúsculas y minúsculas
    caracter = caracter.lower()
    
    #Comprobar si el carácter es una vocal
    if caracter in 'aeiou':
        return True
    else:
        return False

print(es_vocal('a')) #True
print(es_vocal('E')) #True
print(es_vocal('z')) #False
print(es_vocal('O')) #True
