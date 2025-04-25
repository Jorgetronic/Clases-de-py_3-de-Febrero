"""
Calcular el mayor de dos números ingresados por teclado usando un operador
ternario
"""
a = input ( "Entre el primer numero :" )
b = input ("Entre el segundo numero :" )
print("Ambos numeros son iguales, no era la idea") if a == b else print (f"El numero mayor es:{a}"if a > b else f"El numero mayor es: {b}")