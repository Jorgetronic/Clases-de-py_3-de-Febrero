"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario
"""
lista =  input ("Crear una lista de palabras separadas por espacios")
lista = lista.split (" ")
print (f"La lista creada es: {lista}")
buscaPalabra = input ("Que palabra quieres encontrar: ")

def buscaPALABRA (palabra, *lista) :
    print ("La palabra esta en la ista" if palabra in lista else "La palabra no esta en la lista")
    
buscaPALABRA(buscaPalabra,*lista) 