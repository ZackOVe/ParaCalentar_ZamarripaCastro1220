print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def generar_n_caracteres(n, caracter):
    #Repetimos el carácter 'n' veces utilizando la multiplicación de cadenas
    return caracter * n

print(generar_n_caracteres(5, "x"))  #Debería devolver "xxxxx"
print(generar_n_caracteres(3, "*"))  #Debería devolver "***"
print(generar_n_caracteres(7, "-"))  #Debería devolver "-------"
