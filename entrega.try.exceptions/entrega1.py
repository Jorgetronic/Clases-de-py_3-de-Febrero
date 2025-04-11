"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
def division(A,B):
 try:
    Resultado = A/B
    print(Resultado)
 except Exception as e:
        print(f"dividir por cero no esta definido, intentalo nuevamente, error tipo: {e}")
# se solicita la entrada de los numeros a dividir
A = float(input("ingrese el numerador: "))
B = float (input("ingrese el denominador: "))
division(A,B)
