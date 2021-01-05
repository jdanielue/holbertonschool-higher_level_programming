romanos = {'I':1, 'V':5, 'X':10,'L':50,'C':100, 'D': 500, 'M': 1000}
print(romanos)
cadena = "IX"
cero = 0
resultado = 0

for letra in range(0, len(cadena)):
    for letra2 in range(letra, letra + 1):
        if romanos[cadena[letra]] > romanos[cadena[letra2]]  and letra != letra2:
            resultado = romanos[cadena[letra]] + romanos[cadena[letra2]]
            break
        else:
            resultado = romanos[cadena[letra]] + romanos[cadena[letra2]]
            break
    break

print(resultado)
