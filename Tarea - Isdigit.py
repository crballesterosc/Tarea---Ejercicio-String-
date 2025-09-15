var1 = input("Ingrese un numero entero positivo: ")
var2 = input("Ingrese una cadena de texto(sin espacios ni caracteres especiales): ")


#Comando is.digit() - Sirve para verificar si el valor ingresado es un número entero positivo
#Este comando nos permite saber si el valor ingresado es un numero positivo(sin decimales,sin signods, no texto, no espacios)

print("El valor ingresado es: ", var1)
print("Comprobemos si cumple las condiciones del comando isdigit()")
if(var1.isdigit() == True):
    print("TRUE - Este valor es un numero entero positivo")
else:
    print("FALSE - Este valor no es un numero entero positivo")
print()


#Comando is.alpha() - Sirve para verificar si el valor ingresado es una cadena de texto
# Este comando nos permite saber si el valor ingresado es una cadena de texto (sin números)

print()
print("El valor ingresado es: ", var2)
print("Comprobemos si cumple las condiciones del comando isalpha()")
if(var2.isalpha() == True):
    print("TRUE - Este valor es una cadena de texto")
else:
    print("FALSE - Este valor no es una cadena de texto")   