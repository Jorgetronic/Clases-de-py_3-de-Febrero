"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo,
captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
def Suma(A,B):
 try:
    Resultado = A+B
    print(Resultado)
 except TypeError as e:
        print(f"sumar un numero con una cadena es de locos,error tipo:{e}")
# se solicita la entrada de los numeros a dividi
A = int(input("ingrese el numero: "))
B = str (input("ingrese la cadena: "))
Suma(A,B)