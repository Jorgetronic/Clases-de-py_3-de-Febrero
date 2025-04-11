"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
"""


try:
    A = int(input("ingrese el numerador: "))
    B = int(input("ingrese el denominador: "))
    Resultado = A/B
except ValueError as e:
   print (f"Se ha entrado un numero no valido: {e}")
except ZeroDivisionError as e:
   print ( f"se ha dividido por cero: {e}")
else:
   print (Resultado)



