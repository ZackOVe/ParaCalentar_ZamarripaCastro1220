print("")
print("Zamarripa Castro Erick Fabián 3W 1220")
print("")

def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_de_tres(5, 10, 3))  
print(max_de_tres(20, 15, 25)) 
print(max_de_tres(8, 8, 8))     