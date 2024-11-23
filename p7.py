print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def es_palindromo(cadena):
    #Elimina los espacios y convierte todo a minúsculas para una comparación insensible a mayúsculas y minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    #Compara la cadena original con su versión invertida
    return cadena == cadena[::-1]

print(es_palindromo("radar"))  #Debería devolver True
print(es_palindromo("hola"))   #Debería devolver False
print(es_palindromo("A man a plan a canal Panama"))  #Debería devolver True
